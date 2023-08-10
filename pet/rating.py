import typer
from .funcmodule import parse_path
from rich.prompt import Prompt

app = typer.Typer()


# Called when no subcommand is added
@app.callback(invoke_without_command=True)
def main(path: str, ctx: typer.Context, exiftool_path: str = typer.Option(help='Path for exiftool executable', default='exiftool')):
	"""Modify an images rating"""

	# Code runs if command is run with no subcommands (e.g pet rating {{PATH}})
	if ctx.invoked_subcommand is None:
		images = parse_path(path)
		for image in images:
			rating = Prompt.ask('Rating :star:')
			image.update_rating(rating)
