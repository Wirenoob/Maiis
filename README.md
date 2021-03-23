# Maiis
Private bot to work with telegram files

# Usage

fork this github to your repo then sign up to heroku and connect it to your github account and add given var in heroky setting

# Heroku Var

`API_HASH` : <h4>You can get API_HASH in https://my.telegram.org/ sign in there</h4>


`API_ID` : <h4>You can get API_ID in https://my.telegram.org/ sign in there</h4>


`COMMAND_TRIGGER` : <h4>A keyword by which you want to trigger your command like . | or - , </h4><b> (Note donot use * or > as a command it could cause errors)</b>


`DATABASE_URL` : <h4>A url of Mango Database</h4>


`LOG_CHANNEL` : <h4>A log channel chat id create new channel and after that send a message there and forword that message to </h4>@JsonBot <h4> And copy its id and past it on heroku var</h4>


`MASTER_ID` : <h4>Master Is is your chat id copy your message or send message to @JsonBot and copy your chat ID</h4>


`SESSION` : <h4>Session file name without .session extension</h4>


`TOTAL_PIC` : <h4>Total number of pic that imdb command sent</h4>


# Configuration Of Mango DB

<ul>
  <li>First Go to https://www.mongodb.com/ and click on <b>Start Free</b></li>
  
  ![mango1](https://user-images.githubusercontent.com/46376370/112157215-ebcccc00-8bde-11eb-83ef-2cf8501acd3e.png)
  
  <li>Then Click On Sigup With google or you can also fill out the form to create new account</li>
  
  ![mango2](https://user-images.githubusercontent.com/46376370/112157767-6f86b880-8bdf-11eb-8687-52f271d2dda8.png)
  
  <li>After sigup click click <b>I accept the Privacy Policy and the Terms of Service</b> and submit</li>
  
  ![mango3](https://user-images.githubusercontent.com/46376370/112158924-8a0d6180-8be0-11eb-8f91-6aa3802cbae9.png)
  
  <li>After That You will see screen like given below then wait for some time</li>
  
  ![mango4](https://user-images.githubusercontent.com/46376370/112159181-c50f9500-8be0-11eb-9535-c2d2d16f33af.png)
  
  <li>After That Enter <b>Organization</b> and <b>Project Name</b> Anything you want</li>
  
  ![mango5](https://user-images.githubusercontent.com/46376370/112159744-639bf600-8be1-11eb-8515-c97662131568.png)
  
  <li>After that select <b>python</b> and click on <b>continue</b></li>
  
  ![mango6](https://user-images.githubusercontent.com/46376370/112160153-cee5c800-8be1-11eb-88a0-3f3389a64b2e.png)
  
  <li>After that click on create a cluster as shown given below</li>
  
  ![mango7](https://user-images.githubusercontent.com/46376370/112160665-4a477980-8be2-11eb-8efc-92ca2b01c787.png)
  
  <li>Now select <b>Cloud Provider</b> and <b>Region</b></li>
  
  ![mango8](https://user-images.githubusercontent.com/46376370/112161106-b6c27880-8be2-11eb-9d59-cd64438468f9.png)
  
  <li>Now while your cluster is building we would go to other settings for that click on <b>Network Access</b></li>
  
  ![mango9](https://user-images.githubusercontent.com/46376370/112161638-3c462880-8be3-11eb-86cc-de0ed9503b26.png)
  
  <li>Now Click on <b>Add IP address</b></li>
  
  ![mango10](https://user-images.githubusercontent.com/46376370/112161984-8af3c280-8be3-11eb-9dc5-e30958db2bc1.png)
  
  <li>Now Click On <b>ALLOW ACCESS FROM ANYWHERE</b> and then <b>Confirm</b> it will take some time so wait</li>
  
  ![mango11](https://user-images.githubusercontent.com/46376370/112162447-f89fee80-8be3-11eb-94dc-3be4af84385a.png)
  
  <li>When You see <b>Active</b> in <b>Network Access status</b> like given below then click on <b>Database Access</b></li>
  
  ![mango12](https://user-images.githubusercontent.com/46376370/112162942-706e1900-8be4-11eb-9d22-b971bd10e25b.png)
  
  <li>Now click on <b>Add New Database User</b></li>
  
  ![mango13](https://user-images.githubusercontent.com/46376370/112164448-cbecd680-8be5-11eb-9ddc-c178c2057cfc.png)
  
  <li>After that add new user <b>Username</b> and <b>Password</b> and click on <b>Add User</b></li>
  
  ![mango14](https://user-images.githubusercontent.com/46376370/112165077-53d2e080-8be6-11eb-8ea3-a9cfcb2e297c.png)
  
  <li>Now New user is created its time to get database url which you will find in clusters</li>
  
  ![mango15](https://user-images.githubusercontent.com/46376370/112165440-a6140180-8be6-11eb-80f7-1e02dd7a3bcf.png)
  
  <li>As you can see here our cluster is created not its time for connection so click on <b>CONNECT</b></li>
  
  ![mango16](https://user-images.githubusercontent.com/46376370/112165876-0c008900-8be7-11eb-8d8f-25939dd6b618.png)
  
  <li>Now click on <b>Connect your application</b></li>
  
  ![mango16](https://user-images.githubusercontent.com/46376370/112166171-4e29ca80-8be7-11eb-972b-3f504131ca56.png)
  
  <li>Now select <b>python</b> version <b>3.6 or later</b> and copy the url as show below and you will get your url and dont forgot to replace `<password>` with you `password` and `myFirstDatabase` with `data` </li>
  
  ![mango18](https://user-images.githubusercontent.com/46376370/112166947-fe97ce80-8be7-11eb-93e8-cf34d8f60a91.png)
  
</ul>
