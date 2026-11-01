from shopkit.text import slugify


def test_slugify_double_dashes_in_urls():
    assert slugify('Blue T-Shirt (Large)') == 'blue-t-shirt-large'