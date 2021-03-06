from urllib.error import URLError, HTTPError
# ...and from mechanize
from ._auth import \
     HTTPProxyPasswordMgr, \
     HTTPSClientCertMgr
from ._debug import \
     HTTPResponseDebugProcessor, \
     HTTPRedirectDebugProcessor
# crap ATM
## from _gzip import \
##      HTTPGzipProcessor
from urllib.request import \
     AbstractBasicAuthHandler, \
     AbstractDigestAuthHandler, \
     BaseHandler, \
     CacheFTPHandler, \
     FileHandler, \
     FTPHandler, \
     HTTPBasicAuthHandler, \
     HTTPCookieProcessor, \
     HTTPDefaultErrorHandler, \
     HTTPDigestAuthHandler, \
     HTTPErrorProcessor, \
     HTTPHandler, \
     HTTPPasswordMgr, \
     HTTPPasswordMgrWithDefaultRealm, \
     HTTPRedirectHandler, \
     ProxyBasicAuthHandler, \
     ProxyDigestAuthHandler, \
     ProxyHandler, \
     Request, \
     UnknownHandler
from ._http import \
     HTTPEquivProcessor, \
     HTTPRefererProcessor, \
     HTTPRefreshProcessor, \
     HTTPRobotRulesProcessor, \
     RobotExclusionError
from ._opener import MechanizeOpenerDirector, \
     SeekableResponseOpener, \
     build_opener, install_opener, urlopen
