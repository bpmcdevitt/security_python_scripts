[[ -z "$1" ]] && echo "Usage: $0 CVE-YYYY-NNNN" 
	
curl -s http://www.cvedetails.com/cve/$1/ | grep 'meta name="description" content="' | awk -F\" '{print $4}'
