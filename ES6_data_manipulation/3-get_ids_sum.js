export default function getStudentIdsSum(objList) {
  return objList.reduce((acc, i) => acc + i.id, 0);
}
