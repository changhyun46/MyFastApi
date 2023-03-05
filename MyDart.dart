enum Status {
  approved,
  pending,
  rejected,
}

void main() {
  print('Hello Code');
  // variable
  var name = '코드팩토리';
  print(name);

  // 정수
  int number1 = 10;
  print(number1);

  int number3 = -12;
  print(number3);
  print('tes');
  print(number1);

  final DateTime now = DateTime.now();
  print(now);
  // const 빌드타임의 변수값을 지정
  //const DateTime now2 = DateTime.now();

  List<String> blackPink = ['jeni', 'jisu', 'roze', 'risa'];
  print(blackPink);
  blackPink.add('chang');
  print(blackPink);
  blackPink.remove('chang');
  print(blackPink);
  Status sts = Status.approved;
  print(sts);

  Operation operation = subtract;
  int result = operation(10, 20, 30);
  print(result);
  operation = add;
  result = operation(10, 20, 30);
  print(result);
  int result2 = calcul(10, 20, 30, add);
  print(result2);
}

// signature
typedef Operation = int Function(int x, int y, int z);

int add(int x, int y, int z) => x + y + z;
int subtract(int x, int y, int z) => x - y - z;
int calcul(int x, int y, int z, Operation oper) {
  return oper(x, y, z);
}
