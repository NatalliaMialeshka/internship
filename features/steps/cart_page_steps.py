from behave import given, when, then


@when('Reduce the quantity of the product to 0')
def click_on_minus_button(context):
    context.app.cart_page.click_on_minus_button()


@then('Verify the product is removed from cart')
def verify_cart_is_empty(context):
    context.app.cart_page.verify_cart_is_empty()