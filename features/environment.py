from selenium import webdriver
# from features.pages.browsers import desired_cap
# import os
# from features.pages.login_page import LoginDetails
# from features.pages.test_page import TakeTest
#
#
# def before_all(context):
#     for driver_instance in desired_cap:
#         driver_instance['browserstack.debug'] = True
#         driver_instance['resolution'] = '1920x1080'
#         driver_instance['browserstack.autoWait'] = 0
#         driver_instance['browserstack.local'] = True
#         context.driver = webdriver.Remote(
#             command_executor="http://jaipradeesh2:qqhCKW5rEdcxykjHBPyx@hub.browserstack.com:80/wd/hub",
#             desired_capabilities=driver_instance)
#         session_id = context.driver.session_id
#         os.environ['BROWSER_SESSION_ID'] = session_id

# This is required for local testing
#

def before_all(context):
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    context.driver = driver

#
# def before_feature(context, feature):
#     if 'hacker' in feature.tags:
#         LoginDetails(context.driver).hacker_login_details()
#     elif 'test' in feature.tags:
#         LoginDetails(context.driver).recruiter_login_details()
#     elif 'recruiter' or 'codeLab ' in feature.tags:
#         LoginDetails(context.driver).recruiter_login_details()
#     elif 'signup' in feature.tags:
#         LoginDetails(context.driver).open_login_page()
#
#
# def after_feature(context, feature):
#     if 'hacker' in feature.tags:
#         LoginDetails(context.driver).logout_hacker_account()
#     elif 'test' in feature.tags:
#         TakeTest(context.driver).logout_from_test()
#     elif 'recruiter' in feature.tags:
#         LoginDetails(context.driver).logout()
#     elif 'codeLab ' in feature.tags:
#         LoginDetails(context.driver).workspace_logout()
#
#
# def after_all(context):
#     context.driver.quit()
