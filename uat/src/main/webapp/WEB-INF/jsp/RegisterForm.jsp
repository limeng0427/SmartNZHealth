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
<form:form commandName="registerInfo" action="save-register" method="post">
    <fieldset>
        <legend>Register</legend>

        ${empty requestScope.error ? "" : "<p id=\"register_error\" class=\"error\">".concat(requestScope.error).concat("</p>")}


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
        <p>
            <label for="confirmPassword">Confirm Password: </label>
            <form:input id="confirmPassword" path="confirmPassword" type="password"/>
        </p>
        <p id="buttons">
            <input id="reset" type="reset" tabindex="4">
            <input id="submit" type="submit" tabindex="5"
                value="Register">
        </p>
    </fieldset>
</form:form>
</div>
</body>
</html>