import click

from click import echo

from .challenges import challenge, challenges
from .submissions import submissions
from .teams import teams


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    """
    Welcome to the EvalAI CLI.
    """
    if ctx.invoked_subcommand is None:
        welcome_text = ("Welcome to the EvalAI CLI. Use evalai"
                        "--help for viewing all the options")
        echo(welcome_text)


main.add_command(challenges)
main.add_command(challenge)
main.add_command(submissions)
main.add_command(teams)