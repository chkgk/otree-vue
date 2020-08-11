# Reactive page elements with Vue.js for oTree

## Overview
In this demo I show the use of [Vue.js](https://vuejs.org/) to automatically update page elements in reaction to data received via the live send functionality of oTree 3.0.x.

Vue.js allows us to access Javascript variables using special tags. Variables included on a page using these tags automatically update when their values change. Combined with oTree's live send feature, we can automatically update any variables on a page without having to write tedious and repetitive code. This is especially useful when variables need to be updated repeatedly and in more than one place.

Note: Normally, the special tags used by Vue.js are ```{{ varname }}```, which clashes with Django template tags of the same format. Thus, I configured Vue.js to use ```[[ varname ]]``` instead. 

## Demo


## Usage
Include ```VuePage.html``` in your project's ```_templates/global``` folder. Make sure to make your live pages extend ```global/VuePage.html``` instead of the usual ```global/Page.html```. 

The live send method on the ```Group``` model should return a dictionary (```{"key": "value"}```). Elements of this dictionary can then be accessed on the page by using ```[[ live_data.key ]]```. 