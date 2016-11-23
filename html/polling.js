function on_poll_event(event) {
	var xhr = event.target;
	if (xhr.readyState === XMLHttpRequest.DONE) {
		var response = JSON.parse(xhr.responseText);
		sense_value_div.innerHTML = response.sense_valbue;
	}
}

function poll() {
	var xhr = new XMLHttpRequest();
	xhr.onreadystatechange = on_poll_event;
	xhr.open('GET', '/cgi-bin/api-testy.py', true);
	xhr.send();
}

var poller = setInterval(poll, 1000);

var sense_value_div = document.getElementById('part_1_wire_state');
