const ApiRequest = 
{
    /* blueprint; no use in app
    getAttribute = function(attrName)
    {
        
        ajax.sendRequest("/api/attributes", "POST", `{"attribute": "${attrName}", "value": "${attrValue}" }`,
            function(data, status)
            {
                if(status == 201)
                {

                }
            });
        ApiRequest.getAllAttributes();
        
    },
    */
   
    addAttribute = function(attrName, attrValue)
    {

        ajax.sendRequest("/api/attributes", "POST", `{"attribute": "${attrName}", "value": "${attrValue}" }`,
            function(data, status)
            {
                if(status == 201)
                {

                }
            });
        ApiRequest.getAllAttributes();
    },

    updateAttribute = function(attrName, attrValue)
    {
        ajax.sendRequest("/api/attributes", "PUT", `{"attribute": "${attrName}", "value": "${attrValue}" }`,
            function(data, status)
            {
                if(status == 201)
                {

                }
            });
        ApiRequest.getAllAttributes();
    },

    deleteAttribute = function(attrName)
    {
        ajax.sendRequest("/api/attribute", "DELETE", `{"attribute": "${attrName}" }`,
            function(data, status)
            {
                if(status == 204)
                {
                    
                }
            });
        ApiRequest.getAllAttributes();
    },

    getAllAttributes = function()
    {
        ajax.sendRequest("/api/attributes", "GET", null,
            function(data, status)
            {
                if(status == 200)
                {
                    attrs_in = JSON.parse(data)["attributes"];
                    attrs_out = [];
                    for(attrName in attrs)
                    {
                        attr = attrs[attrName];
                        attrs_out.push( AttrModel(attrName, attr.value) );
                    }
                    DataStorage.attrs = attrs_out;
                }
            });
        
    }
}