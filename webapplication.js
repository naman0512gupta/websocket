$(document).ready(function(){
	var socketInterval;
    var websocketurl = "ws://localhost:9090/chat"; //url where your websocket server is running

    ws = new WebSocket(websocketurl); //create socket connection

    //start interval
    //keep trying for server connection if not established
    socketInterval = setInterval(function(){
        retry()
    },2000)
    
    function socketfunctions(){
        ws.onmessage = function(event) {
            var obj = event.data
            notification(obj); // show notification when new message recevied
        };
        function notification(body){
            var notification = new Notification("Heading", { icon: "icon url if required", body: body})
            notification.onshow = function() { setTimeout(notification.close, 15000) } //show notification for 15 seconds
        }
        ws.onerror = function(event){
            console.log("Error ", event)
        }
        ws.onclose = function(){
            //todo on connection close
        };
    }

    socketfunctions() 
    
    function retry(){
        if(ws.readyState === ws.CLOSED){
            ws = new WebSocket(websocketurl);
            socketfunctions()  
        }
    }

});
