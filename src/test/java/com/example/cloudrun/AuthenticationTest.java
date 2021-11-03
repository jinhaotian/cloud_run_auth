/*
 * Copyright 2020 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.example.cloudrun;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.core.StringContains.containsString;

import com.google.api.client.googleapis.javanet.GoogleNetHttpTransport;
import com.google.api.client.http.HttpResponse;
import com.google.api.client.http.HttpTransport;
import com.google.api.client.json.JsonFactory;
import com.google.api.gax.core.NoCredentialsProvider;
import com.google.api.services.iam.v1.Iam;
import com.google.auth.Credentials;
import com.google.cloud.iam.credentials.v1.GenerateAccessTokenResponse;
import com.google.cloud.iam.credentials.v1.GenerateIdTokenResponse;
import com.google.cloud.iam.credentials.v1.IamCredentialsClient;
import com.google.cloud.iam.credentials.v1.IamCredentialsSettings;
import com.google.cloud.iam.credentials.v1.ServiceAccountName;
import com.google.cloud.iam.credentials.v1.SignJwtRequest;
import com.google.cloud.iam.credentials.v1.SignJwtResponse;
import com.google.common.collect.ImmutableList;
import com.google.protobuf.Duration;
import com.google.api.gax.core.GoogleCredentialsProvider;
import com.google.auth.oauth2.GoogleCredentials;

import java.io.IOException;
import java.security.GeneralSecurityException;
import java.util.ArrayList;
import java.util.List;

import org.junit.Assert;
import org.junit.Test;

public class AuthenticationTest {

//  @Test
//  public void canMakeGetRequest() throws IOException {
//    String url = "https://hello-ve5nrmgj5a-uc.a.run.app";
//    HttpResponse response = Authentication.makeGetRequest(url);
//    
//    System.out.println(response.parseAsString());
//    //assertThat(response.parseAsString(), containsString("Example Domain"));
//    assertThat(response.getContentType(), containsString("text/html"));
//    assertThat(response.getStatusCode(), equalTo(200));
//  }
//
//  @Test
//  public void failsMakeGetRequestWithoutProtocol() throws IOException {
//    String url = "example.com/";
//    try {
//      Authentication.makeGetRequest(url);
//    } catch (IllegalArgumentException e) {
//      assertThat(e.getMessage(), containsString("no protocol"));
//    }
//  }
//  
//  @Test
//  public void testJwt() throws IOException {
//      IamCredentialsClient client;
//      IamCredentialsSettings settings =
//              IamCredentialsSettings.newBuilder()
//                  .setCredentialsProvider(GoogleCredentialsProvider.newBuilder().setScopesToApply(
//                          ImmutableList.<String>builder().add("https://www.googleapis.com/auth/cloud-platform").build()).build())
//                  .build();
//       client = IamCredentialsClient.create(settings);
//       
//       ServiceAccountName name = ServiceAccountName.of("jinzi95-seattle", "mcs-service@jinzi95-seattle.iam.gserviceaccount.com");
//       List<String> delegates = new ArrayList<>();
//       String payload = "{\"aud\": \"https://hello-ve5nrmgj5a-uc.a.run.app\",  \"azp\": \"111116024018932792302\",  \"exp\": 1635925860, \"iat\": 1635922260,  \"iss\": \"https://accounts.google.com\",  \"sub\": \"111116024018932792302\"} ";
//
//       SignJwtResponse actualResponse = client.signJwt(name, delegates, payload);
//              
//  }
  @Test
  public void testIdToken() throws IOException {
      
      GoogleCredentials creds = GoogleCredentials.getApplicationDefault();
      System.out.println("access token: "+ creds.getAccessToken());
      System.out.println("id token: "+ creds.getAuthenticationType());
      
      IamCredentialsClient client;
      IamCredentialsSettings settings =
              IamCredentialsSettings.newBuilder()
                  .setCredentialsProvider(GoogleCredentialsProvider.newBuilder().setScopesToApply(
                          ImmutableList.<String>builder().add("https://www.googleapis.com/auth/cloud-platform").build()).build())
                  .build();
       client = IamCredentialsClient.create(settings);
       ServiceAccountName name = ServiceAccountName.of("jinzi95-seattle", "mcs-service@jinzi95-seattle.iam.gserviceaccount.com");
     
       GenerateIdTokenResponse actualResponse = 
               client.generateIdToken("mcs-service@jinzi95-seattle.iam.gserviceaccount.com", 
                       new ArrayList<>(), "https://hello-ve5nrmgj5a-uc.a.run.app/", false);
       System.out.println(actualResponse.getToken());              
  }    

//  @Test
//  public void testAccessToken() throws IOException {
//      IamCredentialsClient client;
//      IamCredentialsSettings settings =
//              IamCredentialsSettings.newBuilder()
//                  .setCredentialsProvider(GoogleCredentialsProvider.newBuilder().setScopesToApply(
//                          ImmutableList.<String>builder().add("https://www.googleapis.com/auth/cloud-platform").build()).build())
//                  .build();
//       client = IamCredentialsClient.create(settings);
//       
//       ServiceAccountName name = ServiceAccountName.of("jinzi95-seattle", "mcs-service@jinzi95-seattle.iam.gserviceaccount.com");
//       Duration lifetime = Duration.newBuilder().build();
//       List<String> scope = new ArrayList<>();
//       GenerateAccessTokenResponse actualResponse =
//               client.generateAccessToken(name, new ArrayList<>(),  
//                       scope,
//                       lifetime);
//     
//       System.out.println(actualResponse.getAccessToken());              
//  }    

  
}
  
