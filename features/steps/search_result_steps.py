from behave import given, when, then


@given('Open CURESKIN main page')
def open_main_page(context):
    context.app.main_page.open_main_page()


@when('Close pop up window')
def close_pop_up(context):
    context.app.main_page.close_pop_up()


@when('Click on search icon')
def click_on_search_icon(context):
    context.app.header.click_on_search()


@when('Input text {text}')
def input_search_text(context, text):
    context.app.header.input_search_text(text)


@then('Verify {text} item(s) is shown')
def verify_search_text_shown(context, text):
    context.app.header.verify_text_search(text)
    context.app.search_result.verify_search_result(text)