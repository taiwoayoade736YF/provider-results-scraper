from web_data_extractor import (
    parse_products,
    remove_duplicates,
    fetch_html,
)
from unittest.mock import Mock, patch

def test_empty_html():
    assert parse_products("", "https://shop.example") == []


def test_remove_duplicates():
    products = [
        {
            "name": "Keyboard",
            "price": "₦15000",
            "url": "https://shop.example/keyboard",
        },
        {
            "name": "Keyboard",
            "price": "₦15000",
            "url": "https://shop.example/keyboard",
        },
    ]

    result = remove_duplicates(products)

    assert len(result) == 1

@patch("web_data_extractor.requests.get")
def test_fetch_html(mock_get):
    mock_response = Mock()
    mock_response.text = "<html>Hello</html>"
    mock_get.return_value = mock_response

    result = fetch_html("https://example.com")

    assert result == "<html>Hello</html>"
    mock_get.assert_called_once()