<?php
/** Just simple code for getting Bio twitter Account  **/
/** Rischan Mafrur  **/
/** April 28 2014   **/


ini_set('display_errors', true);
	


function getBio ($screenName){
 include 'constants.php';
    #require_once('Cache.php');
    require_once('TwitterAPIExchange.php');


     $settings = array(
        'oauth_access_token' => $accessToken,
        'oauth_access_token_secret' => $accessTokenSecret,
        'consumer_key' => $consumerKey,
        'consumer_secret' => $consumerSecret
    );

            $apiUrl = "https://api.twitter.com/1.1/users/show.json";
            $requestMethod = 'GET';
            $getField = '?screen_name=' . $screenName;
     
            $twitter = new TwitterAPIExchange($settings);
            $response = $twitter->setGetfield($getField)
                 ->buildOauth($apiUrl, $requestMethod)
                 ->performRequest();
     
            $data = json_decode($response);
            $followers = $data->followers_count;
            $friends =  $data->friends_count;
            $protected = $data->protected;
            $created_at = $data->created_at;
            $favourites_count = $data->favourites_count;
            $listed_count = $data->listed_count;
            $time_zone = $data->time_zone;
            $statuses_count = $data->statuses_count;
            $location = $data->location;

            $bio = array(
                "followers" => $followers, 
                "friends" => $friends,
                "protected" => $protected,
                "created_at" => $created_at,
                "favourites_count" => $favourites_count,
                "listed" => $listed_count,
                "status"  => $statuses_count,
                "location" => $location,
                "time_zone" =>$time_zone

                );

            return $bio;
  
    
}




?>