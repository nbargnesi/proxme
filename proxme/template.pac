function FindProxyForURL(url, host) {
    var PROXY = "PROXY {{ content['proxy'] }}";
    return "DIRECT";
}
