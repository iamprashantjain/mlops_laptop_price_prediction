// Check if jQuery is loaded; if not, load it dynamically
if (typeof jQuery === 'undefined') {
    var script = document.createElement('script');
    script.src = 'https://code.jquery.com/jquery-3.6.0.min.js'; // or any other version you prefer
    script.onload = function() {
        clickLoadMore();
    };
    document.head.appendChild(script);
} else {
    clickLoadMore();
}

function clickLoadMore() {
    var interval = setInterval(function() {
        var button = $('.sm-load-more'); // Selector for the Load More button
        if (button.length) {
            button.click();
            console.log('Clicked Load More button');
        } else {
            clearInterval(interval);
            console.log('Load More button no longer available');
        }
    }, 2000); // Adjust the interval as needed
}

