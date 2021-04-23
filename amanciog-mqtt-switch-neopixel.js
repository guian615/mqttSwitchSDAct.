// var client  = mqtt.connect({ host:'test.mosquitto.org', port: 8081})
// or
// var client  = mqtt.connect('wss://test.mosquitto.org:8081/mqtt')
// var client  = mqtt.connect({ host:'mqtt.eclipse.org/mqtt', port: 443})
// or
// var client  = mqtt.connect('wss://mqtt.eclipse.org:443/mqtt')

var broker = 'wss://test.mosquitto.org:8081/mqtt';            // it is the broker 
var client  = mqtt.connect(broker);         // the variable client was set to mqtt.connect and passes the broker

var status_header = document.getElementById('status-header') // it stored the document that gets the Element of Id named status-header
 
client.on('connect', function () {
    status_header.innerHTML = 'Connected to '+broker;  // client on connect function and passes the data of status_header  and prints the text containing Connected to concatenated with the broker into the page
    console.log('Connected to '+broker)
})

var pub0_switch = document.getElementById('pub0-switch'); 
pub0_switch.onclick = () => {
    console.log(pub0_switch.checked)                               //this code initiates the variable named pub0_switch and get the value of the element with the id of pub0_switch and gave a condition if the switch at index 0 is clicked and get the data of the topic of cpx/0 or and the payload
    client.publish('cpx/switch0', String(pub0_switch.checked))  
}
var pub1_switch = document.getElementById('pub1-switch');
pub1_switch.onclick = () => {                                        
    console.log(pub1_switch.checked)                                    //this code initiates the variable named pub1_switch and get the value of the element with the id of pub1_switch and gave a condition if the switch at index 1 is clicked and get the data of the topic of cpx/1 or and the payload
    client.publish('cpx/switch1', String(pub1_switch.checked))
}
var pub2_switch = document.getElementById('pub2-switch');
pub2_switch.onclick = () => {                                  //this code initiates the variable named pub2_switch and get the value of the element with the id of pub2_switch and gave a condition if the switch at index 2 is clicked and get the data of the topic of cpx/2 or and the payload
    console.log(pub2_switch.checked)                       
    client.publish('cpx/switch2', String(pub2_switch.checked))
}