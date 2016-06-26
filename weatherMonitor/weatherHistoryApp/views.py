from django.shortcuts import render
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext


def mainPanel(request):
    return render_to_response('main_page.html', context_instance=RequestContext(request))

'''
{
  "response": {
  "version":"0.1",
  "termsofService":"http://www.wunderground.com/weather/api/d/terms.html",
  "features": {
  "history": 1
  }
	},
	"history": {
		"date": {
		"pretty": "November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "12",
		"min": "00",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "20",
		"min": "00",
		"tzname": "UTC"
		},
		"observations": [
		{
		"date": {
		"pretty": "12:04 AM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "00",
		"min": "04",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "8:04 AM GMT on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "08",
		"min": "04",
		"tzname": "UTC"
		},
		"tempm":"16.0", "tempi":"60.8","dewptm":"14.0", "dewpti":"57.2","hum":"88","wspdm":"0.0", "wspdi":"0.0","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"0","wdire":"North","vism":"4.0", "visi":"2.5","pressurem":"1017.5", "pressurei":"30.05","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"0.3", "precipi":"0.01","conds":"Light Rain","icon":"rain","fog":"0","rain":"1","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"SPECI KSFO 210804Z 00000KT 2 1/2SM -RA BR SCT008 BKN014 OVC040 16/14 A3005 RMK AO2 P0001" },
		{
		"date": {
		"pretty": "12:43 AM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "00",
		"min": "43",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "8:43 AM GMT on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "08",
		"min": "43",
		"tzname": "UTC"
		},
		"tempm":"16.0", "tempi":"60.8","dewptm":"14.0", "dewpti":"57.2","hum":"88","wspdm":"7.4", "wspdi":"4.6","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"330","wdire":"NNW","vism":"4.8", "visi":"3.0","pressurem":"1017.5", "pressurei":"30.05","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"1.5", "precipi":"0.06","conds":"Light Rain","icon":"rain","fog":"0","rain":"1","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"SPECI KSFO 210843Z 33004KT 3SM -RA BR SCT005 BKN009 OVC014 16/14 A3005 RMK AO2 P0006" },
		{
		"date": {
		"pretty": "12:55 AM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "00",
		"min": "55",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "8:55 AM GMT on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "08",
		"min": "55",
		"tzname": "UTC"
		},
		"tempm":"15.6", "tempi":"60.1","dewptm":"13.9", "dewpti":"57.0","hum":"90","wspdm":"7.4", "wspdi":"4.6","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"360","wdire":"North","vism":"3.2", "visi":"2.0","pressurem":"1017.6", "pressurei":"30.05","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"2.3", "precipi":"0.09","conds":"Rain","icon":"rain","fog":"0","rain":"1","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"METAR KSFO 210855Z 36004KT 2SM RA BR FEW004 BKN006 OVC011 16/14 A3005 RMK AO2 SLP176 P0009 60023 T01560139 50002" },
		{
		"date": {
		"pretty": "1:32 AM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "01",
		"min": "32",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "9:32 AM GMT on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "09",
		"min": "32",
		"tzname": "UTC"
		},
		"tempm":"16.0", "tempi":"60.8","dewptm":"14.0", "dewpti":"57.2","hum":"88","wspdm":"7.4", "wspdi":"4.6","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"20","wdire":"NNE","vism":"4.8", "visi":"3.0","pressurem":"1017.5", "pressurei":"30.05","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"2.3", "precipi":"0.09","conds":"Light Rain","icon":"rain","fog":"0","rain":"1","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"SPECI KSFO 210932Z 02004KT 3SM -RA BR SCT004 BKN011 OVC025 16/14 A3005 RMK AO2 P0009" },
		{
		"date": {
		"pretty": "1:56 AM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "01",
		"min": "56",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "9:56 AM GMT on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "09",
		"min": "56",
		"tzname": "UTC"
		},
		"tempm":"16.1", "tempi":"61.0","dewptm":"14.4", "dewpti":"57.9","hum":"90","wspdm":"5.6", "wspdi":"3.5","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"150","wdire":"SSE","vism":"11.3", "visi":"7.0","pressurem":"1017.5", "pressurei":"30.05","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"3.0", "precipi":"0.12","conds":"Light Rain","icon":"rain","fog":"0","rain":"1","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"METAR KSFO 210956Z 15003KT 7SM -RA SCT007 SCT015 OVC025 16/14 A3005 RMK AO2 SLP175 P0012 T01610144" },
		{
		"date": {
		"pretty": "2:56 AM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "02",
		"min": "56",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "10:56 AM GMT on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "10",
		"min": "56",
		"tzname": "UTC"
		},
		"tempm":"16.1", "tempi":"61.0","dewptm":"13.9", "dewpti":"57.0","hum":"87","wspdm":"7.4", "wspdi":"4.6","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"170","wdire":"South","vism":"16.1", "visi":"10.0","pressurem":"1017.3", "pressurei":"30.04","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"1.0", "precipi":"0.04","conds":"Overcast","icon":"cloudy","fog":"0","rain":"0","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"METAR KSFO 211056Z 17004KT 10SM FEW010 BKN025 OVC032 16/14 A3004 RMK AO2 RAE54 SLP173 P0004 T01610139" },
		{
		"date": {
		"pretty": "3:56 AM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "03",
		"min": "56",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "11:56 AM GMT on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "11",
		"min": "56",
		"tzname": "UTC"
		},
		"tempm":"16.0", "tempi":"60.8","dewptm":"13.0", "dewpti":"55.4","hum":"82","wspdm":"0.0", "wspdi":"0.0","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"0","wdire":"North","vism":"9.7", "visi":"6.0","pressurem":"1017.2", "pressurei":"30.04","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"-9999.00", "precipi":"-9999.00","conds":"Light Rain","icon":"rain","fog":"0","rain":"1","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"METAR KSFO 211156Z 00000KT 6SM -RA FEW010 BKN025 OVC032 16/13 A3004" },
		{
		"date": {
		"pretty": "4:56 AM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "04",
		"min": "56",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "12:56 PM GMT on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "12",
		"min": "56",
		"tzname": "UTC"
		},
		"tempm":"15.0", "tempi":"59.0","dewptm":"12.8", "dewpti":"55.0","hum":"87","wspdm":"14.8", "wspdi":"9.2","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"250","wdire":"WSW","vism":"11.3", "visi":"7.0","pressurem":"1017.8", "pressurei":"30.06","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"0.8", "precipi":"0.03","conds":"Light Rain","icon":"rain","fog":"0","rain":"1","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"METAR KSFO 211256Z 25008KT 7SM -RA FEW008 BKN027 OVC036 15/13 A3006 RMK AO2 SLP178 P0003 T01500128" },
		{
		"date": {
		"pretty": "5:56 AM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "05",
		"min": "56",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "1:56 PM GMT on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "13",
		"min": "56",
		"tzname": "UTC"
		},
		"tempm":"15.0", "tempi":"59.0","dewptm":"12.8", "dewpti":"55.0","hum":"87","wspdm":"5.6", "wspdi":"3.5","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"290","wdire":"WNW","vism":"16.1", "visi":"10.0","pressurem":"1018.7", "pressurei":"30.09","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"0.5", "precipi":"0.02","conds":"Overcast","icon":"cloudy","fog":"0","rain":"0","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"METAR KSFO 211356Z 29003KT 10SM FEW008 BKN033 OVC045 15/13 A3008 RMK AO2 RAE34 SLP187 P0002 T01500128" },
		{
		"date": {
		"pretty": "6:56 AM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "06",
		"min": "56",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "2:56 PM GMT on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "14",
		"min": "56",
		"tzname": "UTC"
		},
		"tempm":"15.0", "tempi":"59.0","dewptm":"12.8", "dewpti":"55.0","hum":"87","wspdm":"11.1", "wspdi":"6.9","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"260","wdire":"West","vism":"16.1", "visi":"10.0","pressurem":"1019.5", "pressurei":"30.11","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"0.0", "precipi":"0.00","conds":"Light Rain","icon":"rain","fog":"0","rain":"1","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"METAR KSFO 211456Z 26006KT 10SM -RA FEW009 OVC039 15/13 A3011 RMK AO2 RAB21 SLP195 P0000 60005 T01500128 53021" },
		{
		"date": {
		"pretty": "7:56 AM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "07",
		"min": "56",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "3:56 PM GMT on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "15",
		"min": "56",
		"tzname": "UTC"
		},
		"tempm":"15.6", "tempi":"60.1","dewptm":"12.8", "dewpti":"55.0","hum":"83","wspdm":"9.3", "wspdi":"5.8","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"230","wdire":"SW","vism":"16.1", "visi":"10.0","pressurem":"1020.3", "pressurei":"30.13","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"0.0", "precipi":"0.00","conds":"Mostly Cloudy","icon":"mostlycloudy","fog":"0","rain":"0","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"METAR KSFO 211556Z 23005KT 10SM FEW008 SCT031 BKN039 16/13 A3013 RMK AO2 RAE35 SLP203 P0000 T01560128" },
		{
		"date": {
		"pretty": "8:56 AM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "08",
		"min": "56",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "4:56 PM GMT on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "16",
		"min": "56",
		"tzname": "UTC"
		},
		"tempm":"16.1", "tempi":"61.0","dewptm":"12.8", "dewpti":"55.0","hum":"81","wspdm":"18.5", "wspdi":"11.5","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"270","wdire":"West","vism":"16.1", "visi":"10.0","pressurem":"1021.2", "pressurei":"30.16","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"-9999.00", "precipi":"-9999.00","conds":"Mostly Cloudy","icon":"mostlycloudy","fog":"0","rain":"0","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"METAR KSFO 211656Z 27010KT 10SM FEW009 SCT025 BKN030 16/13 A3016 RMK AO2 SLP212 T01610128" },
		{
		"date": {
		"pretty": "9:19 AM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "09",
		"min": "19",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "5:19 PM GMT on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "17",
		"min": "19",
		"tzname": "UTC"
		},
		"tempm":"16.0", "tempi":"60.8","dewptm":"12.0", "dewpti":"53.6","hum":"77","wspdm":"14.8", "wspdi":"9.2","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"280","wdire":"West","vism":"16.1", "visi":"10.0","pressurem":"1021.6", "pressurei":"30.17","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"-9999.00", "precipi":"-9999.00","conds":"Overcast","icon":"cloudy","fog":"0","rain":"0","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"SPECI KSFO 211719Z 28008KT 10SM BKN014 BKN021 OVC040 16/12 A3017 RMK AO2" },
		{
		"date": {
		"pretty": "9:22 AM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "09",
		"min": "22",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "5:22 PM GMT on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "17",
		"min": "22",
		"tzname": "UTC"
		},
		"tempm":"16.0", "tempi":"60.8","dewptm":"12.0", "dewpti":"53.6","hum":"77","wspdm":"14.8", "wspdi":"9.2","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"270","wdire":"West","vism":"16.1", "visi":"10.0","pressurem":"1021.6", "pressurei":"30.17","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"-9999.00", "precipi":"-9999.00","conds":"Overcast","icon":"cloudy","fog":"0","rain":"0","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"SPECI KSFO 211722Z 27008KT 10SM SCT014 BKN030 OVC040 16/12 A3017 RMK AO2" },
		{
		"date": {
		"pretty": "9:56 AM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "09",
		"min": "56",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "5:56 PM GMT on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "17",
		"min": "56",
		"tzname": "UTC"
		},
		"tempm":"16.7", "tempi":"62.1","dewptm":"12.2", "dewpti":"54.0","hum":"75","wspdm":"13.0", "wspdi":"8.1","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"290","wdire":"WNW","vism":"16.1", "visi":"10.0","pressurem":"1021.9", "pressurei":"30.18","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"-9999.00", "precipi":"-9999.00","conds":"Mostly Cloudy","icon":"mostlycloudy","fog":"0","rain":"0","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"METAR KSFO 211756Z 29007KT 10SM FEW008 SCT014 BKN030 17/12 A3018 RMK AO2 SLP219 60005 T01670122 10167 20150 51024" },
		{
		"date": {
		"pretty": "10:56 AM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "10",
		"min": "56",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "6:56 PM GMT on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "18",
		"min": "56",
		"tzname": "UTC"
		},
		"tempm":"17.2", "tempi":"63.0","dewptm":"12.2", "dewpti":"54.0","hum":"72","wspdm":"16.7", "wspdi":"10.4","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"260","wdire":"West","vism":"16.1", "visi":"10.0","pressurem":"1022.1", "pressurei":"30.19","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"-9999.00", "precipi":"-9999.00","conds":"Mostly Cloudy","icon":"mostlycloudy","fog":"0","rain":"0","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"METAR KSFO 211856Z 26009KT 10SM FEW010 BKN030 17/12 A3018 RMK AO2 SLP221 T01720122" },
		{
		"date": {
		"pretty": "11:56 AM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "11",
		"min": "56",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "7:56 PM GMT on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "19",
		"min": "56",
		"tzname": "UTC"
		},
		"tempm":"18.0", "tempi":"64.4","dewptm":"11.0", "dewpti":"51.8","hum":"64","wspdm":"20.4", "wspdi":"12.7","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"260","wdire":"West","vism":"16.1", "visi":"10.0","pressurem":"1021.6", "pressurei":"30.17","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"-9999.00", "precipi":"-9999.00","conds":"Scattered Clouds","icon":"partlycloudy","fog":"0","rain":"0","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"METAR KSFO 211956Z 26011KT 10SM SCT020 18/11 A3017" },
		{
		"date": {
		"pretty": "12:56 PM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "12",
		"min": "56",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "8:56 PM GMT on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "20",
		"min": "56",
		"tzname": "UTC"
		},
		"tempm":"17.2", "tempi":"63.0","dewptm":"10.0", "dewpti":"50.0","hum":"63","wspdm":"24.1", "wspdi":"15.0","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"270","wdire":"West","vism":"16.1", "visi":"10.0","pressurem":"1021.3", "pressurei":"30.16","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"-9999.00", "precipi":"-9999.00","conds":"Scattered Clouds","icon":"partlycloudy","fog":"0","rain":"0","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"METAR KSFO 212056Z 27013KT 10SM FEW020 SCT180 17/10 A3016 RMK AO2 SLP213 T01720100 58006" },
		{
		"date": {
		"pretty": "1:56 PM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "13",
		"min": "56",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "9:56 PM GMT on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "21",
		"min": "56",
		"tzname": "UTC"
		},
		"tempm":"17.2", "tempi":"63.0","dewptm":"10.6", "dewpti":"51.1","hum":"65","wspdm":"18.5", "wspdi":"11.5","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"290","wdire":"WNW","vism":"16.1", "visi":"10.0","pressurem":"1021.3", "pressurei":"30.16","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"-9999.00", "precipi":"-9999.00","conds":"Scattered Clouds","icon":"partlycloudy","fog":"0","rain":"0","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"METAR KSFO 212156Z 29010KT 10SM FEW030 SCT180 17/11 A3016 RMK AO2 SLP213 T01720106" },
		{
		"date": {
		"pretty": "2:56 PM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "14",
		"min": "56",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "10:56 PM GMT on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "22",
		"min": "56",
		"tzname": "UTC"
		},
		"tempm":"16.7", "tempi":"62.1","dewptm":"10.0", "dewpti":"50.0","hum":"65","wspdm":"22.2", "wspdi":"13.8","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"270","wdire":"West","vism":"16.1", "visi":"10.0","pressurem":"1021.5", "pressurei":"30.17","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"-9999.00", "precipi":"-9999.00","conds":"Mostly Cloudy","icon":"mostlycloudy","fog":"0","rain":"0","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"METAR KSFO 212256Z 27012KT 10SM FEW030 BKN180 17/10 A3017 RMK AO2 SLP215 T01670100" },
		{
		"date": {
		"pretty": "3:56 PM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "15",
		"min": "56",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "11:56 PM GMT on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "23",
		"min": "56",
		"tzname": "UTC"
		},
		"tempm":"16.1", "tempi":"61.0","dewptm":"7.8", "dewpti":"46.0","hum":"58","wspdm":"29.6", "wspdi":"18.4","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"280","wdire":"West","vism":"16.1", "visi":"10.0","pressurem":"1021.4", "pressurei":"30.17","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"-9999.00", "precipi":"-9999.00","conds":"Scattered Clouds","icon":"partlycloudy","fog":"0","rain":"0","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"METAR KSFO 212356Z 28016KT 10SM FEW030 SCT180 16/08 A3017 RMK AO2 SLP214 T01610078 10178 20161 50001" },
		{
		"date": {
		"pretty": "4:56 PM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "16",
		"min": "56",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "12:56 AM GMT on November 22, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "22",
		"hour": "00",
		"min": "56",
		"tzname": "UTC"
		},
		"tempm":"14.4", "tempi":"57.9","dewptm":"7.2", "dewpti":"45.0","hum":"62","wspdm":"27.8", "wspdi":"17.3","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"280","wdire":"West","vism":"16.1", "visi":"10.0","pressurem":"1021.5", "pressurei":"30.17","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"-9999.00", "precipi":"-9999.00","conds":"Scattered Clouds","icon":"partlycloudy","fog":"0","rain":"0","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"METAR KSFO 220056Z 28015KT 10SM FEW030 SCT180 14/07 A3017 RMK AO2 SLP215 T01440072" },
		{
		"date": {
		"pretty": "5:56 PM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "17",
		"min": "56",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "1:56 AM GMT on November 22, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "22",
		"hour": "01",
		"min": "56",
		"tzname": "UTC"
		},
		"tempm":"13.9", "tempi":"57.0","dewptm":"8.9", "dewpti":"48.0","hum":"72","wspdm":"24.1", "wspdi":"15.0","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"280","wdire":"West","vism":"16.1", "visi":"10.0","pressurem":"1021.9", "pressurei":"30.18","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"-9999.00", "precipi":"-9999.00","conds":"Partly Cloudy","icon":"partlycloudy","fog":"0","rain":"0","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"METAR KSFO 220156Z 28013KT 10SM FEW180 14/09 A3018 RMK AO2 SLP219 T01390089" },
		{
		"date": {
		"pretty": "6:56 PM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "18",
		"min": "56",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "2:56 AM GMT on November 22, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "22",
		"hour": "02",
		"min": "56",
		"tzname": "UTC"
		},
		"tempm":"13.3", "tempi":"55.9","dewptm":"8.3", "dewpti":"46.9","hum":"72","wspdm":"16.7", "wspdi":"10.4","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"280","wdire":"West","vism":"16.1", "visi":"10.0","pressurem":"1022.2", "pressurei":"30.19","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"-9999.00", "precipi":"-9999.00","conds":"Partly Cloudy","icon":"partlycloudy","fog":"0","rain":"0","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"METAR KSFO 220256Z 28009KT 10SM FEW180 13/08 A3019 RMK AO2 SLP222 T01330083 53007" },
		{
		"date": {
		"pretty": "7:56 PM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "19",
		"min": "56",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "3:56 AM GMT on November 22, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "22",
		"hour": "03",
		"min": "56",
		"tzname": "UTC"
		},
		"tempm":"12.8", "tempi":"55.0","dewptm":"8.3", "dewpti":"46.9","hum":"74","wspdm":"25.9", "wspdi":"16.1","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"280","wdire":"West","vism":"16.1", "visi":"10.0","pressurem":"1022.5", "pressurei":"30.20","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"-9999.00", "precipi":"-9999.00","conds":"Partly Cloudy","icon":"partlycloudy","fog":"0","rain":"0","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"METAR KSFO 220356Z 28014KT 10SM FEW180 13/08 A3020 RMK AO2 SLP225 T01280083" },
		{
		"date": {
		"pretty": "8:56 PM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "20",
		"min": "56",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "4:56 AM GMT on November 22, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "22",
		"hour": "04",
		"min": "56",
		"tzname": "UTC"
		},
		"tempm":"12.2", "tempi":"54.0","dewptm":"7.2", "dewpti":"45.0","hum":"72","wspdm":"18.5", "wspdi":"11.5","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"280","wdire":"West","vism":"16.1", "visi":"10.0","pressurem":"1022.7", "pressurei":"30.20","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"-9999.00", "precipi":"-9999.00","conds":"Clear","icon":"clear","fog":"0","rain":"0","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"METAR KSFO 220456Z 28010KT 10SM CLR 12/07 A3020 RMK AO2 SLP227 T01220072" },
		{
		"date": {
		"pretty": "9:56 PM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "21",
		"min": "56",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "5:56 AM GMT on November 22, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "22",
		"hour": "05",
		"min": "56",
		"tzname": "UTC"
		},
		"tempm":"12.2", "tempi":"54.0","dewptm":"7.8", "dewpti":"46.0","hum":"75","wspdm":"11.1", "wspdi":"6.9","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"290","wdire":"WNW","vism":"16.1", "visi":"10.0","pressurem":"1022.8", "pressurei":"30.21","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"-9999.00", "precipi":"-9999.00","conds":"Clear","icon":"clear","fog":"0","rain":"0","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"METAR KSFO 220556Z 29006KT 10SM CLR 12/08 A3021 RMK AO2 SLP228 T01220078 10156 20122 51007" },
		{
		"date": {
		"pretty": "10:56 PM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "22",
		"min": "56",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "6:56 AM GMT on November 22, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "22",
		"hour": "06",
		"min": "56",
		"tzname": "UTC"
		},
		"tempm":"11.7", "tempi":"53.1","dewptm":"7.8", "dewpti":"46.0","hum":"77","wspdm":"9.3", "wspdi":"5.8","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"290","wdire":"WNW","vism":"16.1", "visi":"10.0","pressurem":"1023.1", "pressurei":"30.22","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"-9999.00", "precipi":"-9999.00","conds":"Clear","icon":"clear","fog":"0","rain":"0","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"METAR KSFO 220656Z 29005KT 10SM CLR 12/08 A3021 RMK AO2 SLP231 T01170078" },
		{
		"date": {
		"pretty": "11:56 PM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "23",
		"min": "56",
		"tzname": "America/Los_Angeles"
		},
		"utcdate": {
		"pretty": "7:56 AM GMT on November 22, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "22",
		"hour": "07",
		"min": "56",
		"tzname": "UTC"
		},
		"tempm":"11.1", "tempi":"52.0","dewptm":"7.8", "dewpti":"46.0","hum":"80","wspdm":"5.6", "wspdi":"3.5","wgustm":"-9999.0", "wgusti":"-9999.0","wdird":"220","wdire":"SW","vism":"16.1", "visi":"10.0","pressurem":"1022.9", "pressurei":"30.21","windchillm":"-999", "windchilli":"-999","heatindexm":"-9999", "heatindexi":"-9999","precipm":"-9999.00", "precipi":"-9999.00","conds":"Clear","icon":"clear","fog":"0","rain":"0","snow":"0","hail":"0","thunder":"0","tornado":"0","metar":"METAR KSFO 220756Z 22003KT 10SM CLR 11/08 A3021 RMK AO2 SLP229 T01110078 401780111" }
		],
		"dailysummary": [
		{ "date": {
		"pretty": "12:00 PM PST on November 21, 2012",
		"year": "2012",
		"mon": "11",
		"mday": "21",
		"hour": "12",
		"min": "00",
		"tzname": "America/Los_Angeles"
		},
		"fog":"0",
            "rain":"1","snow":"0","snowfallm":"0.00", "snowfalli":"0.00","monthtodatesnowfallm":"0.00", "monthtodatesnowfalli":"0.00","since1julsnowfallm":"0.00", "since1julsnowfalli":"0.00","snowdepthm":"", "snowdepthi":"","hail":"0","thunder":"0","tornado":"0","meantempm":"14", "meantempi":"58","meandewptm":"11", "meandewpti":"52","meanpressurem":"1021", "meanpressurei":"30.14","meanwindspdm":"15", "meanwindspdi":"9","meanwdire":"","meanwdird":"275","meanvism":"14", "meanvisi":"9","humidity":"","maxtempm":"18", "maxtempi":"64","mintempm":"11", "mintempi":"52","maxhumidity":"90","minhumidity":"60","maxdewptm":"14", "maxdewpti":"58","mindewptm":"7", "mindewpti":"45","maxpressurem":"1023", "maxpressurei":"30.22","minpressurem":"1017", "minpressurei":"30.04","maxwspdm":"32", "maxwspdi":"20","minwspdm":"0", "minwspdi":"0","maxvism":"16", "maxvisi":"10","minvism":"3", "minvisi":"2","gdegreedays":"8","heatingdegreedays":"7","coolingdegreedays":"0","precipm":"8.13", "precipi":"0.32","precipsource":"","heatingdegreedaysnormal":"10","monthtodateheatingdegreedays":"138","monthtodateheatingdegreedaysnormal":"173","since1sepheatingdegreedays":"349","since1sepheatingdegreedaysnormal":"347","since1julheatingdegreedays":"529","since1julheatingdegreedaysnormal":"460","coolingdegreedaysnormal":"0","monthtodatecoolingdegreedays":"6","monthtodatecoolingdegreedaysnormal":"0","since1sepcoolingdegreedays":"52","since1sepcoolingdegreedaysnormal":"66","since1jancoolingdegreedays":"86","since1jancoolingdegreedaysnormal":"163" }
		]
	}
}
'''