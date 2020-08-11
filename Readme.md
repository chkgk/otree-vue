# Reactive page elements with Vue.js for oTree

## Overview
This repo demonstrates the use of [Vue.js](https://vuejs.org/) to automatically update page elements in reaction to data received via the live send functionality of oTree 3.0.x.

Vue.js allows us to access Javascript variables using special tags. Variables included on a page using these tags automatically update when their values change. Combined with oTree's live send feature, we can automatically update any variables on a page without having to write tedious and repetitive code. This is especially useful when variables need to be updated repeatedly and in more than one place.

Note: Normally, the special tags used by Vue.js are ```{{ varname }}```, which clashes with Django template tags of the same format. Thus, I configured Vue.js to use ```[[ varname ]]``` instead. 

## Demo
A live demo is available [here](https://whispering-sea-09427.herokuapp.com/).
I recommend opening the demo session in split screen mode to see it in action.

## Usage
Include two small scripts in the ```{% block scipts %}``` section of the live page template. Then continue to implement your live sending functions as usual.

```javascript
<script src="https://cdn.jsdelivr.net/npm/vue"></script>
<script type="text/javascript">
    var live_data_received = {live_data: {}};
    liveSocket.onmessage = function (e) {
        live_data_received["live_data"] = JSON.parse(e.data);
    }

    new Vue({
        data: live_data_received,
        el: '._otree-content',
        delimiters: ["[[","]]"]
    });
</script>
``` 

Note: This assumes that the live send method on the ```Group``` model  returns a dictionary (```{"key": "value"}```). Elements of this dictionary can then be accessed on the page by using ```[[ live_data.key ]]```. 