// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example
$.ajax({
	url: '/getpie',
	type: 'GET',
	success: function(response){
    var ctx = document.getElementById("myPieChart");
		var myPieChart = new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels: response['Branch'],
        datasets: [{
          data: response['Placed'],
          backgroundColor: [
            "#25CCF7","#FD7272","#54a0ff","#00d2d3",
            "#1abc9c","#2ecc71","#3498db","#9b59b6","#16a085",
            "#34495e","#27ae60","#2980b9","#8e44ad","#2c3e50",
            "#f1c40f","#e67e22","#e74c3c","#ecf0f1","#95a5a6",
            "#f39c12","#d35400","#c0392b","#bdc3c7","#7f8c8d",
            "#55efc4","#81ecec","#74b9ff","#a29bfe","#dfe6e9",
            "#00b894","#00cec9","#0984e3","#6c5ce7","#ffeaa7",
            "#fab1a0","#ff7675","#fd79a8","#fdcb6e","#e17055",
            "#d63031","#feca57","#5f27cd","#54a0ff","#01a3a4"
        ],
          hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf'],
          hoverBorderColor: "rgba(234, 236, 244, 1)",
        }],
      },
      options: {
        maintainAspectRatio: false,
        tooltips: {
          backgroundColor: "rgb(255,255,255)",
          bodyFontColor: "#858796",
          borderColor: '#dddfeb',
          borderWidth: 1,
          xPadding: 15,
          yPadding: 15,
          displayColors: false,
          caretPadding: 10,
        },
        legend: {
          display: false
        },
        cutoutPercentage: 80,
      },
    });
    
	 }
 });
