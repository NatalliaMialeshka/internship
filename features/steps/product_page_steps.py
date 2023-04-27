from behave import given, when, then


@when('Add product to the cart')
def click_add_to_cart_button(context):
    context.app.product_page.click_add_to_cart_button()


@when('Open Cart from product page')
def click_on_view_cart_button(context):
    context.app.product_page.click_on_view_cart_button()
