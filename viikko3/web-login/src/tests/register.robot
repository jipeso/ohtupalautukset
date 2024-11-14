*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  testaaja
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ab
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Register Credentials
    Register Should Fail With Message  Username length must be at least 3

Register With Valid Username And Too Short Password
    Set Username  testaaja
    Set Password  ab
    Set Password Confirmation  ab
    Submit Register Credentials
    Register Should Fail With Message  Password length must be at least 8

Register With Valid Username And Invalid Password
    Set Username  testaaja
    Set Password  pelkkiakirjaimia
    Set Password Confirmation  pelkkiakirjaimia
    Submit Register Credentials
    Register Should Fail With Message  Password must contain numbers or special characters

Register With Nonmatching Password And Password Confirmation
    Set Username  testaaja
    Set Password  salasana123
    Set Password Confirmation  salasana1
    Submit Register Credentials
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Register Credentials
    Register Should Fail With Message  Username is taken

Login After Succcesful Registration
    Set Username  testaaja
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Register Credentials
    Register Should Succeed
    Click Link  Continue to main page
    Main Page Should Be Open
    Click Button  Logout
    Login Page Should Be Open
    Set Username  testaaja
    Set Password  salasana123
    Submit Login Credentials
    Main Page Should Be Open

Login After Failed Registration
    Set Username  testaaja
    Set Password  salasana123
    Set Password Confirmation  salasana
    Submit Register Credentials
    Register Should Fail With Message  Passwords do not match
    Click Link  Login
    Login Page Should Be Open
    Set Username  testaaja
    Set Password  salasana123
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Register Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}