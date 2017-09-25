object CenturyFromYear extends App {
  def centuryfromyear(year: Int): Int = {
    if (year % 100 == 0) {
      year/100
    } else {
      (year/100) + 1
    }
  }

  println(centuryfromyear(1900))
}
