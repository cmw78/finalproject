import random

def getCourses():    
    filename = 'courses.txt'
    f = open(filename, "r")
    courseDict = {}
    for line in f.readlines():
        line = line.strip()
        lineData = line.split(',')
        courseID = lineData[0].strip()
        courseName = lineData[1].strip()
        courseDict[courseID] = courseName
    f.close()
    return courseDict
   
def getStudents():
	filename = 'students.txt'
	f = open(filename, "r")
	studentsDict = {'cmw78' : 'Christina Williams', 'smk44' : 'Stephen Kwok'}
	maxIDNumber = 100
	for line in f.readlines():
		line = line.strip()
		if len(line) > 2:
			studentID = line[:3] + str(random.randint(0, maxIDNumber))
			studentsDict[studentID] = line
	f.close()
	return studentsDict

def getFriends(studentsDict):
	friendTuples = []
	studentIDList = studentsDict.keys()
	maxFriends = 10
	while len(studentIDList) > 1:
		numFriends = random.randint(0, min([len(studentIDList) - 1, maxFriends]))
		friends = set([studentIDList[random.randint(1, min([maxFriends - 1, len(studentIDList) - 1]))] for i in range(numFriends)])
		for friend in friends:
			friendTuples.append((studentIDList[0], friend))
		studentIDList = studentIDList[1:]
	return friendTuples

def getProfessors():
	filename = 'professors.txt'
	f = open(filename, 'r')
	professorsDict = {}
	maxIDNumber = 100
	for line in f.readlines():
		professorName = line.strip()
		professorSplit = professorName.split(' ')
		professorID = professorSplit[0][0] + professorSplit[1][0] + str(random.randint(0, maxIDNumber))
		professorsDict[professorID] = professorName 
	f.close()
	return professorsDict

def getTeaches(professorsDict, coursesDict):
	professors = professorsDict.keys()
	teachesTuples = []
	for courseID in coursesDict.keys():
		maxProfessors = 3
		for i in range(maxProfessors):
			if random.randint(0,1) == 0:
				professorID = professors[random.randint(0, len(professors) - 1)]
				semester = getRandomSemester()
				teachesTuples.append((courseID, professorID, semester))
	return teachesTuples

def getBookbag(coursesDict, studentsDict):
	courses = coursesDict.keys()
	students = studentsDict.keys()
	bookbagTuples = []
	numTuples = 500
	for i in range(numTuples):
		course = courses[random.randint(1, len(courses) - 1)]
		student = students[random.randint(1, len(students) - 1)]
		bookbagTuples.append((course, student))
	return list(set(bookbagTuples))

def getTaken(coursesDict, studentsDict):
	ratings = [-1, 0, 1]
	courses = coursesDict.keys()
	students = studentsDict.keys()
	numTuples = 200
	visitedPairs = set([])
	takenTuples = []
	for i in range(numTuples):
		course = courses[random.randint(0, len(courses)-1)]
		student = students[random.randint(0, len(students) - 1)]
		if (course, student) not in visitedPairs:
			rating = ratings[random.randint(0, len(ratings)-1)]
			semester = getRandomSemester()
			takenTuples.append((course, student, rating, semester))
			visitedPairs.add((course, student))
	return takenTuples
	
def getTaking(coursesDict, studentsDict):
	takingTuples = []
	courses = coursesDict.keys()
	maxClasses = 4
	for student in studentsDict.keys():
		studentCourses = set([courses[random.randint(0, len(courses)-1)] for i in range(maxClasses)])
		for course in studentCourses:
			takingTuples.append((course, student))
	return takingTuples
	
def getRandomSemester():
	semesterOptions = ['S', 'F']
	semesterYears = ['14', '15', '16']
	return semesterOptions[random.randint(0, len(semesterOptions) - 1)] + semesterYears[random.randint(0, len(semesterYears) - 1)]
		
def generateTableStudents(studentsDict):	
	f = open('tableStudents.txt', 'w')
	for k, v in studentsDict.iteritems():
		f.write(k + " " + v + '\n')
	f.close()	
		
def generateTableProfessors(professorsDict):
	f = open('tableProfessors.txt', 'w')
	for k, v in professorsDict.iteritems():
		f.write(k + " " + v + '\n')
	f.close()
		
def generateTableCourses(coursesDict):
	f = open('tableCourses.txt', 'w')
	for k, v in coursesDict.iteritems():
		f.write(k + " " + v + '\n')
	f.close()
	
def generateTableIsFriendsWith(friendsTuples):
	f = open('tableIsFriendsWith.txt', 'w')
	for tuple in friendsTuples:
		f.write(tuple[0] + " " + tuple[1] + '\n')
	f.close()
	
def generateTableTeaches(teachesTuples):
	f = open('tableTeaches.txt', 'w')
	for tuple in teachesTuples:
		f.write(tuple[0] + " " + tuple[1] + " " + tuple[2] + '\n')
	f.close()
	
def generateTableTaking(takingTuples):
	f = open('tableTaking.txt', 'w')
	for tuple in takingTuples:
		f.write(tuple[0] + " " + tuple[1] + '\n')
	f.close()
	
def generateTableBookbag(bookbagTuples):
	f = open('tableBookbag.txt', 'w')
	for tuple in bookbagTuples:
		f.write(tuple[0] + " " + tuple[1] + '\n')
	f.close()
	
def generateTableTaken(takenTuples):
	f = open('tableTaken.txt', 'w')
	for tuple in takenTuples:
		f.write(tuple[0] + " " + tuple[1] + " " + str(tuple[2]) + " " + tuple[3] + '\n')
	f.close()
	
def generateQueriesStudents():
	data = open('tableStudents.txt', 'r')
	f = open('queriesStudents.txt', 'w')
	for line in data.readlines():
		lineValues = line.strip().split(' ')
		ID = addQuotes(lineValues[0])
		name = addQuotes(lineValues[1])
		f.write("INSERT INTO {0} VALUES({1}, {2})".format('Student', ID, name))
		f.write('\n')
	data.close()
	f.close()
	
def generateQueriesProfessors():
	data = open('tableProfessors.txt', 'r')
	f = open('queriesProfessors.txt', 'w')
	for line in data.readlines():
		line = line.strip()
		lastSpace = line.find(' ')
		ID = addQuotes(line[:lastSpace])
		name = addQuotes(line[lastSpace + 1 :])
		f.write("INSERT INTO {0} VALUES({1}, {2})".format('Professor', ID, name))
		f.write('\n')
	data.close()
	f.close()
		
def generateQueriesCourses():
	data = open('courses.txt', 'r')
	f = open('queriesCourses.txt', 'w')
	for line in data.readlines():
		line = line.strip()
		lineValues = line.split(',')
		ID = addQuotes(line[0].strip())
		name = addQuotes(lineValues[1].strip())
		f.write("INSERT INTO {0} VALUES({1}, {2})".format('Course', ID, name))
		f.write('\n')
	data.close()
	f.close()

def generateQueriesIsFriendsWith():
	data = open('tableIsFriendsWith.txt', 'r')
	f = open('queriesIsFriendsWith.txt', 'w')
	for line in data.readlines():
		line = line.strip()
		lineValues = line.split(' ')
		ID1 = addQuotes(lineValues[0].strip())
		ID2 = addQuotes(lineValues[1].strip())
		f.write("INSERT INTO {0} VALUES({1}, {2})".format('IsFriendsWith', ID1, ID2))
		f.write('\n')
	data.close()
	f.close()
	
def generateQueriesTaken():
	data = open('tableTaken.txt', 'r')
	f = open('queriesTaken.txt', 'w')
	for line in data.readlines():
		line = line.strip()
		lineValues = line.split(' ')
		courseID = addQuotes(lineValues[0].strip() + " " + lineValues[1].strip())
		studentID = addQuotes(lineValues[2].strip())
		rating = lineValues[3].strip()
		semester = addQuotes(lineValues[4].strip())
		f.write("INSERT INTO {0} VALUES({1}, {2}, {3}, {4})".format('Taken', courseID, studentID, rating, semester))
		f.write('\n')
	data.close()
	f.close()
	
def generateQueriesTeaches():
	data = open('tableTeaches.txt', 'r')
	f = open('queriesTeaches.txt', 'w')
	for line in data.readlines():
		line = line.strip()
		lineValues = line.split(' ')
		courseID = addQuotes(lineValues[0].strip() + " " + lineValues[1].strip())
		professorID = addQuotes(lineValues[2].strip())
		semester = addQuotes(lineValues[3].strip())
		f.write("INSERT INTO {0} VALUES({1}, {2}, {3})".format('Teaches', courseID, professorID, semester))
		f.write('\n')
	data.close()
	f.close()
	
def generateQueriesBookbag():
	data = open('tableBookbag.txt', 'r')
	f = open('queriesBookbag.txt', 'w')
	for line in data.readlines():
		line = line.strip()
		lineValues = line.split(' ')
		courseID = addQuotes(lineValues[0].strip() + " " + lineValues[1].strip())
		studentID = addQuotes(lineValues[2].strip())
		f.write("INSERT INTO {0} VALUES({1}, {2})".format('Bookbag', courseID, studentID))
		f.write('\n')
	data.close()
	f.close()
	
def generateQueriesTaking():
	data = open('tableTaking.txt', 'r')
	f = open('queriesTaking.txt', 'w')
	for line in data.readlines():
		line = line.strip()
		lineValues = line.split(' ')
		courseID = addQuotes(lineValues[0].strip() + " " + lineValues[1].strip())
		studentID = addQuotes(lineValues[2].strip())
		f.write("INSERT INTO {0} VALUES({1}, {2})".format('Taking', courseID, studentID))
		f.write('\n')
	data.close()
	f.close()

	
def addQuotes(s):
	return "'" + s + "'"
		
if __name__ == '__main__':
	studentsDict = getStudents()
	coursesDict = getCourses()
	professorsDict = getProfessors()
	friendsTuples = getFriends(studentsDict)
	teachesTuples = getTeaches(professorsDict, coursesDict)
	bookbagTuples = getBookbag(coursesDict, studentsDict)
	takenTuples = getTaken(coursesDict, studentsDict)
	takingTuples = getTaking(coursesDict, studentsDict)
	generateTableStudents(studentsDict)
	generateTableProfessors(professorsDict)
	generateTableCourses(coursesDict)
	generateTableIsFriendsWith(friendsTuples)
	generateTableTeaches(teachesTuples)
	generateTableBookbag(bookbagTuples)
	generateTableTaken(takenTuples)
	generateTableTaking(takingTuples)
	generateQueriesStudents()
	generateQueriesProfessors()
	generateQueriesCourses()
	generateQueriesIsFriendsWith()
	generateQueriesTeaches()
	generateQueriesTaken()
	generateQueriesBookbag()
	generateQueriesTaking()