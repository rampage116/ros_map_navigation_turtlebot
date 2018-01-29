
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point 
from sound_play.libsoundplay import SoundClient

class map_navigation():
	
	def choose(self):

		choice='q'
		
		rospy.loginfo("|-------------------------------|")
		rospy.loginfo("|PRESSE A KEY:")
		rospy.loginfo("|'0': H108 ")
		rospy.loginfo("|'1': H106 ")
		rospy.loginfo("|'2': Fire_Exit_Back ")
		rospy.loginfo("|'3': H105 ")
                rospy.loginfo("|'4': H107 ")
                rospy.loginfo("|'5': H104 ")
                rospy.loginfo("|'6': H109 ")
                rospy.loginfo("|'7': H103 ")
                rospy.loginfo("|'8': H101 ")

                rospy.loginfo("|'q': Quit ")
		rospy.loginfo("|-------------------------------|")
		rospy.loginfo("|WHERE TO GO?")
		choice = input()
		return choice

	def __init__(self): 

		sc = SoundClient()
		path_to_sounds = "/home/ros/Desktop/gaitech_edu-master/src/sounds/"

		# declare the coordinates of interest 
		self.xH108 = 7.01
		self.yH108 = 5.52
		self.xH106 = 2.76
		self.yH106 = 2.18
		self.xFire_Exit_Back = 0.75
		self.yFire_Exit_Back = 1.21
		self.xH105 = 1.76
		self.yH105 = 0.22
                self.xH107 = 6.78
                self.yH107 = 3.92
                self.xH104 = 10.26
                self.yH104 = 1.05
                self.xH109 = 12.56
                self.yH109 = 3.26
                self.xH103 = 14.53
                self.yH103 = 1.34
                self.xH101 = 18.97
                self.yH101 = 1.75


		self.goalReached = False
		# initiliaze
        	rospy.init_node('map_navigation', anonymous=False)
		choice = self.choose()
		
		if (choice == 0):

			self.goalReached = self.moveToGoal(self.xH108, self.yH108)
		
		elif (choice == 1):

			self.goalReached = self.moveToGoal(self.xH106, self.yH106)

		elif (choice == 2):
			
			self.goalReached = self.moveToGoal(self.xFire_Exit_Back, self.yFire_Exit_Back)
		
		elif (choice == 3):

			self.goalReached = self.moveToGoal(self.xH105, self.yH105)

                elif (choice == 4):

                        self.goalReached = self.moveToGoal(self.xH107, self.yH107)

                elif (choice == 5):

                        self.goalReached = self.moveToGoal(self.xH104, self.yH104)

                elif (choice == 6):

                        self.goalReached = self.moveToGoal(self.xH109, self.yH109)

                elif (choice == 7):

                        self.goalReached = self.moveToGoal(self.xH103, self.yH103)

                elif (choice == 8):

                        self.goalReached = self.moveToGoal(self.xH101, self.yH101)



		if (choice!='q'):

			if (self.goalReached):
				rospy.loginfo("Congratulations!")
				#rospy.spin()

				sc.playWave(path_to_sounds+"Ringing_Phone.wav")
#				rosrun sound_play say.py "hi, i am Marlyine"
				#rospy.spin()

			else:
				rospy.loginfo("Hard Luck!")
				sc.playWave(path_to_sounds+"buzzer_x.wav")
		
		while choice != 'q':
			choice = self.choose()
			if (choice == 0):

				self.goalReached = self.moveToGoal(self.xH108, self.yH108)
		
			elif (choice == 1):

				self.goalReached = self.moveToGoal(self.xOffice1, self.yOffice1)

			elif (choice == 2):
		
				self.goalReached = self.moveToGoal(self.xFire_Exit_Back, self.yFire_Exit_Back)
		
			elif (choice == 3):

				self.goalReached = self.moveToGoal(self.xH105, self.yH105)

                        elif (choice == 4):

                                self.goalReached = self.moveToGoal(self.xH107, self.yH107)

                        elif (choice == 5):

                                self.goalReached = self.moveToGoal(self.xH104, self.yH104)

                        elif (choice == 6):

                                self.goalReached = self.moveToGoal(self.xH109, self.yH109)

                        elif (choice == 7):

                                self.goalReached = self.moveToGoal(self.xH103, self.yH103)

                        elif (choice == 8):

                                self.goalReached = self.moveToGoal(self.xH101, self.yH101)



			if (choice!='q'):

				if (self.goalReached):
					rospy.loginfo("Congratulations!")
					#rospy.spin()

					sc.playWave(path_to_sounds+"Ringing_Phone.wav")

				else:
					rospy.loginfo("Hard Luck!")
					sc.playWave(path_to_sounds+"buzzer_x.wav")


	def shutdown(self):
        # stop turtlebot
        	rospy.loginfo("Quit program")
        	rospy.sleep()

	def moveToGoal(self,xGoal,yGoal):

		#define a client for to send goal requests to the move_base server through a SimpleActionClient
		ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

		#wait for the action server to come up
		while(not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
			rospy.loginfo("Waiting for the move_base action server to come up")
		

		goal = MoveBaseGoal()

		#set up the frame parameters
		goal.target_pose.header.frame_id = "map"
		goal.target_pose.header.stamp = rospy.Time.now()

		# moving towards the goal*/

		goal.target_pose.pose.position =  Point(xGoal,yGoal,0)
		goal.target_pose.pose.orientation.x = 0.0
		goal.target_pose.pose.orientation.y = 0.0
		goal.target_pose.pose.orientation.z = 0.0
		goal.target_pose.pose.orientation.w = 1.0

		rospy.loginfo("Sending goal location ...")
		ac.send_goal(goal)

		ac.wait_for_result(rospy.Duration(60))

		if(ac.get_state() ==  GoalStatus.SUCCEEDED):
			rospy.loginfo("You have reached the destination")	
			return True
	
		else:
			rospy.loginfo("The robot failed to reach the destination")
			return False

if __name__ == '__main__':
    try:
	
	rospy.loginfo("You have reached the destination")
        map_navigation()
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("map_navigation node terminated.")
