<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE html>
<html>
<head>
<title>Register</title>
<style type="text/css">@import url("<c:url value="/css/main.css"/>");</style>
</head>
<body>

<div id="global">
<form:form commandName="loginInfo" action="try-login" method="post">
    <fieldset>
        <legend>Login</legend>

        ${empty requestScope.error ? "" : "<p id=\"error\" class=\"error\">".concat(requestScope.error).concat("</p>")}

        <p>
            <label for="email">Email: </label>
            <form:input id="email" path="email" type="email"
                cssErrorClass="error"/>
            <form:errors path="email" cssClass="error"/>
        </p>
        <p>
            <label for="password">Password: </label>
            <form:input id="password" path="password" type="password"/>
        </p>

        <p id="buttons">
            <input id="reset" type="reset" tabindex="4">
            <input id="submit" type="submit" tabindex="5"
                value="Login">
        </p>
    </fieldset>
</form:form>
</div>
</body>
</html>