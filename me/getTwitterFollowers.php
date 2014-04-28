<?php
	ini_set('display_errors', true);
	

	include 'constants.php';
    require_once('Cache.php');
    require_once('TwitterAPIExchange.php');
  

     $settings = array(
        'oauth_access_token' => $accessToken,
        'oauth_access_token_secret' => $accessTokenSecret,
        'consumer_key' => $consumerKey,
        'consumer_secret' => $consumerSecret
    );
 
   $cache = new Cache();
  
    // get follower count from cache
    $numberOfFollowers = $cache->read('cfTwitterFollowers.cache');
    // cache version does not exist or expired
  
        // forming data for request
        $apiUrl = "https://api.twitter.com/1.1/users/show.json";
        $requestMethod = 'GET';
        $getField = '?screen_name=rischanmafrur';
 
        $twitter = new TwitterAPIExchange($settings);
        $response = $twitter->setGetfield($getField)
             ->buildOauth($apiUrl, $requestMethod)
             ->performRequest();
 
        $followers = json_decode($response);
        $numberOfFollowers = $followers->followers_count;
        echo $numberOfFollowers;
  
        // cache for an hour
        $cache->write('cfTwitterFollowers.cache', $numberOfFollowers, 1*60*60);
    

?>