#include <stdio.h>
#include <curl/curl.h>
#include <string.h>

CURLcode nextLink(char * page){
  char* url = "https://en.wikipedia.org/api/rest_v1/page/html/Bogosort";
  CURL *curl = curl_easy_init();
  if(curl){
    CURLcode res;
    curl_easy_setopt(curl, CURLOPT_URL, url);
    res = curl_easy_perform(curl);
    curl_easy_cleanup(curl);

    return res;
  }
 
}

int main(){
  char * text = (char *) nextLink("Thing");
  
  char * href_start = strstr(text, "<a ");
  if (href_start){
    printf("Found a at:i \n");
    printf((char *) href_start);
  }
  return 1;
}
