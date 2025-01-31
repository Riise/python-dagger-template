"""Dagger functions

This file contains the Dagger functions that define the steps of the pipeline.
"""

import dagger
from dagger import dag, function, object_type

CONTAINER = "python:3.12-slim"


@object_type
class DaggerMain:
    """Dagger class"""

    @function
    def ci_container(self, prj: dagger.Directory) -> dagger.Container:
        """Build a ready-to-use development environment"""

        # create a Dagger cache volume for dependencies
        # node_cache = dag.cache_volume("node")

        return (
            dag.container()
            .from_(CONTAINER)
            .with_directory(
                ".",
                prj,
                exclude=[".git", ".pytest_cache", ".devcontainer", "dagger"],
            )
            .with_exec(["chmod", "+x", "./scripts/ci-container-setup.sh"])
            .with_exec(["./scripts/ci-container-setup.sh"])
        )

    @function
    async def pylint(self, prj: dagger.Directory) -> str:
        """Return the result of running unit tests"""

        return await self.ci_container(prj).with_exec(["pylint", "src/"]).stdout()

    @function
    async def bandit(self, prj: dagger.Directory) -> str:
        """Return the result of running unit tests"""

        return (
            await self.ci_container(prj)
            .with_exec(["bandit", "-c", "./bandit.yml", "-r", "./src/"])
            .stdout()
        )

    @function
    async def safety(self, prj: dagger.Directory) -> str:
        """Return the result of running Safety CLI"""

        return await self.ci_container(prj).with_exec(["safety", "check"]).stdout()

    @function
    async def pip_audit(self, prj: dagger.Directory) -> str:
        """Return the result of running pip-audit Python package known vulnerabilities scanner"""

        return (
            await self.ci_container(prj)
            .with_exec(["pip-audit", "-r", "requirements.txt"])
            .stdout()
        )

    @function
    async def pytest(self, prj: dagger.Directory) -> str:
        """Return the result of running unit tests"""

        return await self.ci_container(prj).with_exec(["pytest", "tests/"]).stdout()

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

        output = await self.safety(prj)
        output += await self.pip_audit(prj)

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
        output += await self.safety(prj)

        output += await self.pytest(prj)

        return output

    # endregion --- Pipelines & Composite Steps -----------------------------------------------
