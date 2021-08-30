Feature: 

	Background:
		#@PRECOND_DEM-10
		Given when i open the app
		Then user will start doing something

	@TEST_DEM-2
	Scenario: chkchk
		Given open app
		When user is pointing url abcde
		Then user opens the app
	@TEST_DEM-1
	Scenario: demo test
		Given open app again
		When user logs in
		Then user is logged in
