export default function updateStudentGradeByCity(objList, city, newGrades) {
  const filteredStudents = objList.filter(student => student.location === city);

  const result = filteredStudents.map(student => {
    let grade = 'N/A';

    for (const g of newGrades) {
      if (g.studentId === student.id) {
        grade = g.grade
      }
    }

    return {
      ...student,
      grade: grade
    };
  });
}
