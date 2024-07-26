<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .form-container {
            width: px;
            margin: 0 auto;
        }
        .form-field {
            margin-bottom: 10px;
        }
        .form-field label {
            display: block;
            margin-bottom: 5px;
        }
        .form-field input {
            width: 100%;
            padding: 5px;
        }
        .submit-button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <form action="/submit" method="post">
            <div class="form-field">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username">
            </div>
            <div class="form-field">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password">
            </div>
            <input class="submit-button" type="submit" value="Submit">
        </form>
    </div>
</body>
</html>
