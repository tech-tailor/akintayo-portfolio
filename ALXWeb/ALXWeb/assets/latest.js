function userpilotInitiator(){if(window.userpilot&&(window.userpilot.initializing||window.userpilot.initialized))return{init:function(){}};var t={token:"",version:"1.478",endpoint:"api.userpilot.io/socket/",domain:"js.userpilot.io",accessibility:1,integrations_interfaces:{},noConflictId:"",proxy:"socket"};return window.userpilotCallMethods={identify:[],locale:[],group:[],anonymous:[],reload:[],track:[],trigger:[],end:[],reset:[],clean:[],getData:[],suppress:[],on:[],off:[],once:[],log:[],theme:[]},window.userpilot={init:function(){var e;for(e in window.userpilotSettings||(window.userpilotSettings={}),"NX-f6e84007"==window.userpilotSettings.token&&(window.userpilotSettings.version="1.473"),t)window.userpilotSettings.hasOwnProperty(e)||(window.userpilotSettings[e]=t[e]);var o=document.createElement("script"),n=window.userpilotSettings.domain||"js.userpilot.io";try{sessionStorage.getItem("temp-userpilot-token")&&(window.userpilotSettings.token=sessionStorage.getItem("temp-userpilot-token")),sessionStorage.getItem("temp-userpilot-version")?(window.userpilotSettings.version=sessionStorage.getItem("temp-userpilot-version"),o.src="https://"+n+"/sdk/version/"+window.userpilotSettings.version+"/app.js?ver="+(new Date).getTime()):o.src="https://"+n+"/sdk/version/"+window.userpilotSettings.version+"/app.js"}catch(t){o.src="https://"+n+"/sdk/version/"+window.userpilotSettings.version+"/app.js"}o.async="true",document.querySelector("head").appendChild(o)},identify:function(t,e){window.userpilotCallMethods.identify.push({userid:t,data:e})},locale:function(t){window.userpilotCallMethods.locale.push({data:t})},group:function(t,e){window.userpilotCallMethods.group.push({companyId:t,data:e})},reload:function(t){window.userpilotCallMethods.reload.push({events:t})},log:function(){window.userpilotCallMethods.log.push({log:1})},end:function(t){window.userpilotCallMethods.end.push({content:t})},track:function(t,e){window.userpilotCallMethods.track.push({title:t,meta:e})},trigger:function(t){window.userpilotCallMethods.trigger.push({token:t})},anonymous:function(){window.userpilotCallMethods.anonymous.push({anonymous:1})},reset:function(){window.userpilotCallMethods.reset.push({reset:1})},isRunning:function(){return{}},suppress:function(){window.userpilotCallMethods.suppress.push({suppress:1})},clean:function(){window.userpilotCallMethods.clean.push({clean:1})},on:function(t,e){window.userpilotCallMethods.on.push({name:t,fn:e})},off:function(t){window.userpilotCallMethods.off.push({name:t})},once:function(t,e){window.userpilotCallMethods.once.push({name:t,fn:e})},theme:function(t){window.userpilotCallMethods.theme.push({name:t})},initializing:function(){return!0}},window.userpilot}window.userpilotSettings&&-1!==["NX-6c7255d7","NX-917089a3","NX-8d110747","39dr79r9","NX-b72d04f4"].indexOf(window.userpilotSettings.token)&&(window.$USERPILOTQALL$=document.querySelectorAll.bind(document),window.$USERPILOTQ$=document.querySelector.bind(document));var userpilotInitiatorSDK=new userpilotInitiator;userpilotInitiatorSDK.init();