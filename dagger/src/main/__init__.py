"""PythonDaggerTemplate functions

This file contains the Dagger functions that define the steps of the pipeline.
"""

import dagger
from dagger import dag, function, object_type

PYTHON_VERSION = "3.10"

# NOTE: it's recommended to move your code into other files in this package
# and keep __init__.py for imports only, according to Python's convention.
# The only requirement is that Dagger needs to be able to import a package
# called "main", so as long as the files are imported here, they should be
# available to Dagger.


@object_type
class PythonDaggerTemplate:
    """Dagger class"""

    # @function
    # def container_echo(self, string_arg: str) -> dagger.Container:
    #     """Returns a container that echoes whatever string argument is provided"""
    #     return dag.container().from_("alpine:latest").with_exec(["echo", string_arg])

    # @function
    # async def grep_dir(self, directory_arg: dagger.Directory, pattern: str) -> str:
    #     """Returns lines that match a pattern in the files of the provided Directory"""
    #     return await (
    #         dag.container()
    #         .from_("alpine:latest")
    #         .with_mounted_directory("/mnt", directory_arg)
    #         .with_workdir("/mnt")
    #         .with_exec(["grep", "-R", pattern, "."])
    #         .stdout()
    #     )

    @function
    def ci_container(self, prj: dagger.Directory) -> dagger.Container:
        """Build a ready-to-use development environment"""

        # create a Dagger cache volume for dependencies
        # node_cache = dag.cache_volume("node")

        return (
            dag.container()
            .from_(f"python:{PYTHON_VERSION}-slim")
            .with_directory(
                ".",
                prj,
                exclude=[".git", ".pytest_cache", ".devcontainer", "dagger"],
            )
            .with_exec(["./scripts/ci-container-setup.sh"])
        )

    @function
    async def pylint(self, prj: dagger.Directory) -> str:
        """Return the result of running unit tests"""

        return await self.ci_container(prj).with_exec(["pylint", "src/"]).stdout()

    @function
    async def pytest(self, prj: dagger.Directory) -> str:
        """Return the result of running unit tests"""

        return await self.ci_container(prj).with_exec(["pytest", "tests/"]).stdout()

    @function
    async def bandit(self, prj: dagger.Directory) -> str:
        """Return the result of running unit tests"""

        return await self.ci_container(prj).with_exec(["bandit", "-r", "src/"]).stdout()

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
    async def build(self, prj: dagger.Directory) -> str:
        """Return the result of building the project"""

        return (
            await (
                self.ci_container(prj)
                # call the build script
                .with_exec(["./scripts/build.sh"])
                # capture and return the command output
                .stdout()
            )
        )
