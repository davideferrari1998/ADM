<%@ page import="java.util.*"%><% response.setContentType("application/json");
%>[
{	
	"sensor":"1",
	"type":"PM10",
	"timestamp":"<%=(new Date(session.getLastAccessedTime()))%>",
	"value":"5"
},
{	
	"sensor":"2",
	"type":"Temperature",
	"timestamp":"<%=(new Date(session.getLastAccessedTime()))%>",
	"value":"20"
},
{	
	"sensor":"3",
	"type":"Temperature",
	"timestamp":"<%=(new Date(session.getLastAccessedTime()))%>",
	"value":"50"
},
{	
	"sensor":"4",
	"type":"PM10",
	"timestamp":"<%=(new Date(session.getLastAccessedTime()))%>",
	"value":"2"
}
]