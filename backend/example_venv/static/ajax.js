


const ajax = 
{
    sendRequest =  function (url, method = "GET", data = null, onSuccess = null)
    {
        req = new XMLHttpRequest()
        
        req.open(method, url, true)
        
        req.send(data);

        req.onreadystatechange()
        {
            if (req.readystate === XMLHttpRequest.DONE)
            {
                if (typeof onSuccess === 'function')
                {
                    if(onSuccess.length == 2) onSuccess(req.responseText, req.status);
                    else if(onSuccess.length == 1) onSuccess(req.responseText);
                    else if(onSuccess.length == 0) onSuccess();
                    else console.log ("ajax: reqest "+url+" done; function has to have 0 - 2 parameters "+onSuccess.length+" specified");
                } 
                else { console.log ("ajax: reqest "+url+" done; no onSuccess function specified"); }
            }
        }

    }
}