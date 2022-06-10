<%@ page import="java.util.*"%><% response.setContentType("application/json");
%>{	
	"sensor":"2",
	"type":"Temperature",
	"timestamp":"<%=(new Date(session.getLastAccessedTime()))%>",
	"value":"20"
}