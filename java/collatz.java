
public class collatz {
    public static void main(String[] args) {
        _Collatz();
    }
    public static void _Collatz() {
        long total_n = 1000;
        long max_n = 0;
        int max_count = 0;
        long time = Instant.now().getEpochSecond();
        for (int n = 1; n <= total_n; n++) {
            int count = 0;
            long i = n;
            while (i != 1) {
                if (i % 2 == 0) {
                    i = i / 2;
                } else {
                    i = 3 * i + 1;
                }
                count++;
            }
            if (count > max_count) {
                max_count = count;
                max_n = n;
            }
        }

        System.out.println(max_n + " " + max_count + " " + (Instant.now().getEpochSecond() - time) + "s" );
    }
}