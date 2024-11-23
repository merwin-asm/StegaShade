import sys
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.box import ROUNDED
from stega_shade import (
    simple_shade_stega,
    undo_simple_shade_stega,
    protected_shade_stega,
    undo_protected_shade_stega,
)

console = Console()

def display_help():
    """
    Displays the help message with available commands.
    """
    table = Table(title="Stega Shade - Command Reference", box=ROUNDED, show_edge=False)
    table.add_column("Command", style="cyan bold", justify="right")
    table.add_column("Description", style="green")

    table.add_row(
        "encode_simple <image_path> <output_path> \"<data>\"",
        "Encodes data into an image using simple steganography.",
    )
    table.add_row(
        "decode_simple <image_path>",
        "Decodes data from an image created with simple steganography.",
    )
    table.add_row(
        "encode_protected <image_path> <output_path> \"<data>\" \"<password>\"",
        "Encodes data into an image with password protection.",
    )
    table.add_row(
        "decode_protected <image_path> \"<password>\"",
        "Decodes password-protected data from an image.",
    )
    table.add_row("help", "Displays this help message.")

    console.print(
        Panel.fit(
            table,
            title="📷 Stega Shade CLI 📷",
            subtitle="Your Image Steganography Toolkit",
            border_style="magenta",
        )
    )


def main():
    """
    Main function to handle command-line arguments and execute steganography operations.
    """
    if len(sys.argv) < 2:
        console.print("[bold red]Error:[/] No command provided. Use 'help' for usage details.")
        sys.exit(1)

    command = sys.argv[1]

    if command == "help":
        display_help()
    elif command == "encode_simple":
        if len(sys.argv) != 5:
            console.print("[bold red]Error:[/] Incorrect arguments for encode_simple.")
            sys.exit(1)
        image_path, output_path, data = sys.argv[2], sys.argv[3], sys.argv[4]
        try:
            simple_shade_stega(image_path, output_path, data)
            console.print(f"[green]Successfully encoded data into '{output_path}'.[/green]")
        except Exception as e:
            console.print(f"[bold red]Error:[/] {str(e)}")
    elif command == "decode_simple":
        if len(sys.argv) != 3:
            console.print("[bold red]Error:[/] Incorrect arguments for decode_simple.")
            sys.exit(1)
        image_path = sys.argv[2]
        try:
            decoded_data = undo_simple_shade_stega(image_path)
            console.print(f"[green]Decoded Data:[/] {decoded_data}")
        except Exception as e:
            console.print(f"[bold red]Error:[/] {str(e)}")
    elif command == "encode_protected":
        if len(sys.argv) != 6:
            console.print("[bold red]Error:[/] Incorrect arguments for encode_protected.")
            sys.exit(1)
        image_path, output_path, data, password = sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
        try:
            protected_shade_stega(image_path, output_path, data, password)
            console.print(f"[green]Successfully encoded protected data into '{output_path}'.[/green]")
        except Exception as e:
            console.print(f"[bold red]Error:[/] {str(e)}")
    elif command == "decode_protected":
        if len(sys.argv) != 4:
            console.print("[bold red]Error:[/] Incorrect arguments for decode_protected.")
            sys.exit(1)
        image_path, password = sys.argv[2], sys.argv[3]
        try:
            decoded_data = undo_protected_shade_stega(image_path, password)
            console.print(f"[green]Decoded Data:[/] {decoded_data}")
        except Exception as e:
            console.print(f"[bold red]Error:[/] {str(e)}")
    else:
        console.print(f"[bold red]Error:[/] Unknown command '{command}'. Use 'help' for usage details.")
        sys.exit(1)


if __name__ == "__main__":
    main()
