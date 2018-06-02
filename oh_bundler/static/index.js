define([
    'base/js/namespace',
    'jquery',
    'base/js/utils',
    'base/js/dialog'
], function(Jupyter, $, utils, dialog) {

    function load_ipython_extension() {
	$('a').filter(function(index) { return $(this).text() === "Deploy as"; }).html("Share Notebook");
    }

    return {
	load_ipython_extension: load_ipython_extension
    };

});
