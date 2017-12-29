from flask import Flask, request, render_template, redirect


app = Flask(__name__)
app.config['DEBUG'] = True

app_username = ''
app_username_error = ''

app_password = ''
app_password_error = ''

app_v_password = ''
app_v_password_error = ''

app_email_option = ''
app_email_option_error = ''


@app.route("/")
def display_initial_user_signup():
    username     = ''
    password     = ''
    v_password   = ''
    email_option = ''

    return render_template("user-signup.html")


@app.route("/validate-signup", methods=['POST'])
def validate_signup():
    app_username     = request.form["username"]
    app_password     = request.form["password"]
    app_v_password   = request.form["v_password"]
    app_email_option = request.form["email_option"]

    app_username_error = edit_username(app_username)
    app_password_error = edit_password(app_password)
    if app_password_error:
        app_v_password_error = ''
    else:    
        app_v_password_error = edit_v_password(app_password, app_v_password)
    app_email_option_error   = edit_email_option(app_email_option)

    if ( app_username_error   ) or ( app_password_error ) or \
       ( app_v_password_error ) or ( app_email_option_error ): 

        return render_template('user-signup.html',
            username           = app_username, 
            username_error     = app_username_error,
            
            password           = '', 
            password_error     = app_password_error,
            
            v_password         = '',
            v_password_error   = app_v_password_error,
            
            email_option       = app_email_option, 
            email_option_error = app_email_option_error )
    else:         
        return render_template('welcome.html', username = app_username)       


def edit_username(editUsername):
    editUsernameError = ''
    if (editUsername == ''):
        editUsernameError = 'Please enter Username'

    elif (len(editUsername) < 3) or (len(editUsername) > 20):
        editUsernameError = 'Username must not be less than 3, or greater than 20 characters'
    elif ' ' in editUsername:
        editUsernameError = 'Username must not contain spaces'
   
    return(editUsernameError)


def edit_password(editPassword):
    editPasswordError = ''
    if (editPassword == ''):
        editPasswordError = 'Please enter Password'

    elif (len(editPassword) < 3) or (len(editPassword) > 20):
        editPasswordError = 'Password must not be less than 3, or greater than 20 characters'
    elif ' ' in editPassword:
        editPasswordError = 'Password must not contain spaces'
        
    return(editPasswordError)


def edit_v_password(editPassword, editVPassword):
    
    if (editPassword == editVPassword):
        editVPasswordError = ''
    else:    
        editVPasswordError = 'Verify Password not entered, or Password and Verify Password do not match' 

    return(editVPasswordError)


def edit_email_option(editEmailOption):
    editEmailOptionError = ''

    if (len(editEmailOption) == 0):
        editEmailOptionError = ''
    elif (not ('@' in editEmailOption)) or (not ('.' in editEmailOption)):
       
        editEmailOptionError = '"If Email Option entered, then it must contain both a "." and a "@"'
    elif (len(editEmailOption) < 3) or (len(editEmailOption) > 20):
       
        editEmailOptionError = 'If Email Option entered, then it must not be less than 3, or greater than 20 characters'

    return(editEmailOptionError)

app.run()