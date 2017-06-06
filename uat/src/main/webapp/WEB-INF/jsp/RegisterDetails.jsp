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

<fieldset>
    <legend>Register Successful</legend>
    <p id="register_successful_message">
        Congruatulations! Please <a href="<c:url value="/login"/>"> login </a> to start use.
    </p>
</fieldset>

</div>
</body>
</html>