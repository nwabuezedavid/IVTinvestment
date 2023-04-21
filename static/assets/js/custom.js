
$( document ).ready(function() {
	$('#cal__amount').on('change keyup',function () {
		var amount = $(this).val();
		if(!isNaN(amount)){
			if(amount >= 10 && amount <= 999) {
				var percent = 10;
				var daily = amount/100*percent;
				daily = "$" + daily.toFixed(2);
				
				var weekly = amount/100*percent;
				weekly = weekly*7;
				weekly = "$" + weekly.toFixed(2);
				
				var monthly = amount/100*percent;
				monthly = monthly*30;
				monthly = "$" + monthly.toFixed(2);
				
				var yearly = amount/100*percent;
				yearly = yearly*365;
				yearly = "$" + yearly.toFixed(2);
				
				$('#calc_daily').html(daily);
				$('#calc_weekly').html(weekly);
				$('#calc_monthly').html(monthly);
				$('#calc_yearly').html(yearly);
			} else if(amount >= 1000 && amount <= 3000)	{
				var percent = 8;
				var daily = amount/100*percent;
				daily = "$" + daily.toFixed(2);
				
				var weekly = amount/100*percent;
				weekly = weekly*7;
				weekly = "$" + weekly.toFixed(2);
				
				var monthly = amount/100*percent;
				monthly = monthly*30;
				monthly = "$" + monthly.toFixed(2);
				
				var yearly = amount/100*percent;
				yearly = yearly*365;
				yearly = "$" + yearly.toFixed(2);
				
				$('#calc_daily').html(daily);
				$('#calc_weekly').html(weekly);
				$('#calc_monthly').html(monthly);
				$('#calc_yearly').html(yearly);
			}
			else if(amount >= 3001 && amount <= 6000)	{
				var percent = 9;
				var daily = amount/100*percent;
				daily = "$" + daily.toFixed(2);
				
				var weekly = amount/100*percent;
				weekly = weekly*7;
				weekly = "$" + weekly.toFixed(2);
				
				var monthly = amount/100*percent;
				monthly = monthly*30;
				monthly = "$" + monthly.toFixed(2);
				
				var yearly = amount/100*percent;
				yearly = yearly*365;
				yearly = "$" + yearly.toFixed(2);
				
				$('#calc_daily').html(daily);
				$('#calc_weekly').html(weekly);
				$('#calc_monthly').html(monthly);
				$('#calc_yearly').html(yearly);
			}
			else if(amount >= 6001 && amount <= 10000)	{
				var percent = 10;
				var daily = amount/100*percent;
				daily = "$" + daily.toFixed(2);
				
				var weekly = amount/100*percent;
				weekly = weekly*7;
				weekly = "$" + weekly.toFixed(2);
				
				var monthly = amount/100*percent;
				monthly = monthly*30;
				monthly = "$" + monthly.toFixed(2);
				
				var yearly = amount/100*percent;
				yearly = yearly*365;
				yearly = "$" + yearly.toFixed(2);
				
				$('#calc_daily').html(daily);
				$('#calc_weekly').html(weekly);
				$('#calc_monthly').html(monthly);
				$('#calc_yearly').html(yearly);
			}
			else if(amount >= 10001 && amount <= 50000)	{
				var percent = 12;
				var daily = amount/100*percent;
				daily = "$" + daily.toFixed(2);
				
				var weekly = amount/100*percent;
				weekly = weekly*7;
				weekly = "$" + weekly.toFixed(2);
				
				var monthly = amount/100*percent;
				monthly = monthly*30;
				monthly = "$" + monthly.toFixed(2);
				
				var yearly = amount/100*percent;
				yearly = yearly*365;
				yearly = "$" + yearly.toFixed(2);
				
				$('#calc_daily').html(daily);
				$('#calc_weekly').html(weekly);
				$('#calc_monthly').html(monthly);
				$('#calc_yearly').html(yearly);
			}
			else {
				$('#calc_daily').html('N/A');
				$('#calc_weekly').html('N/A');
				$('#calc_monthly').html('N/A');
				$('#calc_yearly').html('N/A');
			}
		}
		
	});
});