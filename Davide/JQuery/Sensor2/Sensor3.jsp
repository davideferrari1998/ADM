<%@ page import="java.util.*"%><% response.setContentType("application/json");
%>{	
	"sensor":"3",
	"type":"Temperature",
	"timestamp":"<%=(new Date(session.getLastAccessedTime()))%>",
	"value":"50"
}