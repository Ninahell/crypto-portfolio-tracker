from app.cli import create_parser


def test_parser_add_command():
    parser = create_parser()

    args = parser.parse_args([
        "add",
        "--asset", "BTC",
        "--amount", "1",
        "--price", "50000"
    ])

    assert args.asset == "BTC"
    assert args.amount == 1
