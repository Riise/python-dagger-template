"""Dagger functions

This file contains the Dagger functions that define the steps of the pipeline.
"""

import dagger
from dagger import dag, function, object_type

CONTAINER = "python:3.14-slim"


@object_type
class DaggerMain:
    """Dagger class"""

    @function
    def ci_container(self, prj: dagger.Directory) -> dagger.Container:
        """Build a ready-to-use development environment"""

        # create a Dagger cache volume for dependencies
        # node_cache = dag.cache_volume("node")

        # python:3.14-slim has no curl, so fetch the uv binary directly from its
        # official image instead of running the network-dependent install script.
        uv_binary = dag.container().from_("ghcr.io/astral-sh/uv:latest").file("/uv")

        return (
            dag.container()
            .from_(CONTAINER)
            .with_file("/usr/local/bin/uv", uv_binary, permissions=0o755)
            .with_directory(
                ".",
                prj,
                exclude=[".git", ".pytest_cache", ".devcontainer", "dagger", ".venv"],
            )
            .with_exec(["chmod", "+x", "./scripts/ci-container-setup.sh"])
            .with_exec(["./scripts/ci-container-setup.sh"])
        )

    @function
    async def pylint(self, prj: dagger.Directory) -> str:
        """Return the result of running unit tests"""

        return (
            await self.ci_container(prj)
            .with_exec(["uv", "run", "--no-sync", "pylint", "src/"])
            .stdout()
        )

    @function
    async def bandit(self, prj: dagger.Directory) -> str:
        """Return the result of running unit tests"""

        return (
            await self.ci_container(prj)
            .with_exec(["uv", "run", "--no-sync", "bandit", "-c", "./bandit.yml", "-r", "./src/"])
            .stdout()
        )

    @function
    async def pip_audit(self, prj: dagger.Directory) -> str:
        """Return the result of running pip-audit Python package known vulnerabilities scanner"""

        return (
            await self.ci_container(prj)
            .with_exec(["uv", "run", "--no-sync", "pip-audit", "--path", ".venv"])
            .stdout()
        )

    @function
    async def pytest(self, prj: dagger.Directory) -> str:
        """Return the result of running unit tests"""

        return (
            await self.ci_container(prj)
            .with_exec(["uv", "run", "--no-sync", "pytest", "tests/"])
            .stdout()
        )

    # region --- Pipelines & Composite Steps --------------------------------------------------

    @function
    async def lint(self, prj: dagger.Directory) -> str:
        """Code linting and security scanning"""

        output = await self.pylint(prj)
        output += await self.bandit(prj)

        return output

    @function
    async def scan(self, prj: dagger.Directory) -> str:
        """Dependency vulnerability scanning"""

        output = await self.pip_audit(prj)

        return output

    @function
    async def test(self, prj: dagger.Directory) -> str:
        """Unit test"""

        output = await self.pytest(prj)

        return output

    @function
    async def ci(self, prj: dagger.Directory) -> str:
        """Full CI pipeline"""

        output = await self.pylint(prj)
        output += await self.bandit(prj)

        output += await self.pip_audit(prj)

        output += await self.pytest(prj)

        return output

    # endregion --- Pipelines & Composite Steps -----------------------------------------------
