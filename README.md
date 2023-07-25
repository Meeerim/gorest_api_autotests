## API Autotests project for gorest.co.in
<p align="center">
  <img width="50%" title="Gorest" src="images/gorest.png">
</p>
24/7 online fake GraphQL and REST API service for quick testing and prototyping of web and android applications.

### Tools and a technologies used
<p  align="center">
<code><img width="5%" title="Python" src="images/python.png"></code>
<code><img width="5%" title="Pycharm" src="images/pycharm.png"></code>
<code><img width="5%" title="Pytest" src="images/pytest.png"></code>
<code><img width="5%" title="Allure Report" src="images/allure_report.png"></code>
<code><img width="5%" title="Allure TestOps" src="images/allure_testops.png"></code>
<code><img width="5%" title="Jira" src="images/jira.png"></code>
<code><img width="5%" title="Jenkins" src="images/jenkins.png"></code>
<code><img width="5%" title="Requests" src="images/requests.png"></code>
<code><img width="5%" title="Telegram Bot" src="images/tg.png"></code>
<code><img width="5%" title="GitHub" src="images/github.png"></code>
</p>
<br> 

### Specific scenarios that were checked
* Get Users Details - Verify Successful Response and Schema
* Create New User - Verify Successful User Creation and ID
* Update User Email - Verify Successful Email Update
* Update User Details - Verify Successful User Details Update
* Delete User - Verify Successful User Deletion
* User posts - Verify Successful Response and Schema,ID
<br>

<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="images/jenkins.png"> Running tests from Jenkins
### [Job](https://jenkins.autotests.cloud/job/meerim_diplom_work_api_tests/)
##### Main page of the build:
![This is an image](images/screenshots/jenkins.png)
##### After the build is done the test results are available in Allure Report and Allure TestOps


<!-- Allure report -->

### <img width="3%" title="Allure Report" src="images/allure_report.png"> Allure report
##### From main page of Allure report can see  :

>- <code><strong>*ALLURE REPORT*</strong></code> -date and time of the test, overall number of launched tests,
>- <code><strong>*TREND*</strong></code> - trend of running tests for all runs
>- <code><strong>*SUITES*</strong></code> - distribution of tests by suites
>- <code><strong>*CATEGORIES*</strong></code> - distribution of unsuccessful tests by defect types

![This is an image](images/screenshots/allure_dashboard.png)


##### On the page the list of the tests grouped by suites with status shown for each test.
![This is an image](images/screenshots/allure_suites.png)


<!-- Allure TestOps -->

### <img width="3%" title="Allure TestOps" src="images/allure_testops.png"> Allure TestOps Integration
### [Dashboard](https://allure.autotests.cloud/project/2086/dashboards)
##### Results are uploaded there and the automated test-cases can be automatically updated accordingly to the recent changes in the code.
![This is an image](notion_autotest_api/resources/images/screenshots/allure_testops_dashboard.png)

Test-cases in the project are imported and constantly updated from the code,
so there is no need in complex process of synchronization manual test-cases and autotests.\
It is enough to create and update an autotest in the code and the test-case in TMS always will be in actual state.\
Manual test-cases also can be added in TMS in case of need(via web interface or via code).

![This is an image](notion_autotest_api/resources/images/screenshots/allure_testops_suites.png)


<!-- Jira -->

### <img width="3%" title="Jira" src="images/jira.png"> Jira integration
##### After configuration TestOps we can integrate results launches in Jira

![This is an image](images/screenshots/jira.png)


<!-- Telegram -->

### <img width="3%" title="Telegram" src="images/tg.png"> Telegram Notifications
##### Telegram bot sends a brief report to a specified telegram chat by results of each build.

![This is an image](images/screenshots/tg_bot.png)
