import java.util.*;

/*
 * COMPETITIVE CODING - I
 * Complete Java Code Bank - Sessions 1 to 15
 *
 * Format:
 *   - Each problem has a separate method.
 *   - Methods are written in simple Java / LeetCode style.
 *   - Put your own main() and test cases as required.
 */

public class Main {

    // =========================================================
    // SESSION 1 - INTRODUCTION / BASIC JAVA
    // =========================================================

    // Factorial using loop
    static int factorialLoop(int n) {
        int ans = 1;
        for (int i = 1; i <= n; i++)
            ans *= i;
        return ans;
    }

    // Sum of array
    static int arraySum(int[] a) {
        int sum = 0;
        for (int x : a)
            sum += x;
        return sum;
    }

    // Find maximum element
    static int findMaximum(int[] a) {
        int max = a[0];
        for (int x : a)
            max = Math.max(max, x);
        return max;
    }

    // =========================================================
    // SESSION 2 - RECURSION
    // =========================================================

    // 1. Factorial
    static int factorial(int n) {
        if (n == 0 || n == 1)
            return 1;
        return n * factorial(n - 1);
    }

    // 2. Power a^b
    static long power(int a, int b) {
        if (b == 0)
            return 1;
        return a * power(a, b - 1);
    }

    // 3. Print increasing
    static void printIncreasing(int n) {
        if (n == 0)
            return;
        printIncreasing(n - 1);
        System.out.print(n + " ");
    }

    // 4. Print decreasing
    static void printDecreasing(int n) {
        if (n == 0)
            return;
        System.out.print(n + " ");
        printDecreasing(n - 1);
    }

    // 5. Sum of digits
    static int sumDigits(int n) {
        if (n == 0)
            return 0;
        return n % 10 + sumDigits(n / 10);
    }

    // 6. Sum of array using recursion
    static int recursiveArraySum(int[] a, int index) {
        if (index == a.length)
            return 0;
        return a[index] + recursiveArraySum(a, index + 1);
    }

    // 7. Reverse String using recursion
    static String reverseString(String s) {
        if (s.length() <= 1)
            return s;
        return reverseString(s.substring(1)) + s.charAt(0);
    }

    // 8. Remove / Add parentheses - simple balanced generation
    static void generateParentheses(int n, int open, int close, String cur,
            List<String> ans) {
        if (cur.length() == 2 * n) {
            ans.add(cur);
            return;
        }

        if (open < n)
            generateParentheses(n, open + 1, close, cur + "(", ans);

        if (close < open)
            generateParentheses(n, open, close + 1, cur + ")", ans);
    }

    static List<String> generateParenthesis(int n) {
        List<String> ans = new ArrayList<>();
        generateParentheses(n, 0, 0, "", ans);
        return ans;
    }

    // 9. Expression Add Operators
    static void addOperators(String num, int target, int index,
            long value, long prev, String expr,
            List<String> ans) {
        if (index == num.length()) {
            if (value == target)
                ans.add(expr);
            return;
        }

        for (int j = index; j < num.length(); j++) {
            if (j > index && num.charAt(index) == '0')
                break;

            long cur = Long.parseLong(num.substring(index, j + 1));

            if (index == 0) {
                addOperators(num, target, j + 1, cur, cur,
                        "" + cur, ans);
            } else {
                addOperators(num, target, j + 1, value + cur, cur,
                        expr + "+" + cur, ans);

                addOperators(num, target, j + 1, value - cur, -cur,
                        expr + "-" + cur, ans);

                addOperators(num, target, j + 1,
                        value - prev + prev * cur,
                        prev * cur, expr + "*" + cur, ans);
            }
        }
    }

    static List<String> expressionAddOperators(String num, int target) {
        List<String> ans = new ArrayList<>();
        addOperators(num, target, 0, 0, 0, "", ans);
        return ans;
    }

    // =========================================================
    // SESSION 3 - RECURSION II
    // =========================================================

    // 1. Fibonacci
    static int fibonacci(int n) {
        if (n <= 1)
            return n;
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    // 2. Tower of Hanoi
    static void towerOfHanoi(int n, char source, char helper, char destination) {
        if (n == 0)
            return;

        towerOfHanoi(n - 1, source, destination, helper);
        System.out.println("Move disk " + n + " from " + source + " to " + destination);
        towerOfHanoi(n - 1, helper, source, destination);
    }

    // 3. Pivot Index
    static int pivotIndex(int[] nums) {
        int total = 0;
        for (int x : nums)
            total += x;

        int left = 0;
        for (int i = 0; i < nums.length; i++) {
            int right = total - left - nums[i];
            if (left == right)
                return i;
            left += nums[i];
        }
        return -1;
    }

    // 4. Remove Duplicates from Sorted Array
    static int removeDuplicates(int[] nums) {
        if (nums.length == 0)
            return 0;

        int k = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) {
                nums[k++] = nums[i];
            }
        }
        return k;
    }

    // 5. Pascal Triangle II
    static List<Integer> getRow(int rowIndex) {
        List<Integer> row = new ArrayList<>();
        long value = 1;

        for (int i = 0; i <= rowIndex; i++) {
            row.add((int) value);
            value = value * (rowIndex - i) / (i + 1);
        }
        return row;
    }

    // 6. Pow(x, n) - fast recursion
    static double myPow(double x, long n) {
        if (n == 0)
            return 1.0;

        if (n < 0) {
            x = 1 / x;
            n = -n;
        }

        double half = myPow(x, n / 2);

        if (n % 2 == 0)
            return half * half;
        return half * half * x;
    }

    // 7. Letter Tile Possibilities
    static int letterTilePossibilities(String tiles) {
        int[] freq = new int[26];
        for (char c : tiles.toCharArray())
            freq[c - 'A']++;

        return tileDFS(freq);
    }

    static int tileDFS(int[] freq) {
        int count = 0;

        for (int i = 0; i < 26; i++) {
            if (freq[i] == 0)
                continue;

            count++;
            freq[i]--;
            count += tileDFS(freq);
            freq[i]++;
        }

        return count;
    }

    // 8. K-th Symbol in Grammar
    static int kthGrammar(int n, int k) {
        if (n == 1)
            return 0;

        int parent = kthGrammar(n - 1, (k + 1) / 2);

        if (k % 2 == 1)
            return parent;
        return 1 - parent;
    }

    // =========================================================
    // SESSION 4 - ARRAY I
    // =========================================================

    // 1. Maximum Subarray - Kadane
    static int maxSubArray(int[] nums) {
        int current = nums[0];
        int best = nums[0];

        for (int i = 1; i < nums.length; i++) {
            current = Math.max(nums[i], current + nums[i]);
            best = Math.max(best, current);
        }
        return best;
    }

    // 2. Maximum Product Subarray
    static int maxProduct(int[] nums) {
        int max = nums[0];
        int min = nums[0];
        int ans = nums[0];

        for (int i = 1; i < nums.length; i++) {
            int x = nums[i];

            if (x < 0) {
                int temp = max;
                max = min;
                min = temp;
            }

            max = Math.max(x, max * x);
            min = Math.min(x, min * x);
            ans = Math.max(ans, max);
        }
        return ans;
    }

    // 3. Maximum Average Subarray I
    static double findMaxAverage(int[] nums, int k) {
        int sum = 0;
        for (int i = 0; i < k; i++)
            sum += nums[i];

        int maxSum = sum;

        for (int i = k; i < nums.length; i++) {
            sum += nums[i] - nums[i - k];
            maxSum = Math.max(maxSum, sum);
        }

        return (double) maxSum / k;
    }

    // 4. Maximum Sum Circular Subarray
    static int maxSubarraySumCircular(int[] nums) {
        int total = 0;
        int curMax = 0, maxSum = nums[0];
        int curMin = 0, minSum = nums[0];

        for (int x : nums) {
            curMax = Math.max(x, curMax + x);
            maxSum = Math.max(maxSum, curMax);

            curMin = Math.min(x, curMin + x);
            minSum = Math.min(minSum, curMin);

            total += x;
        }

        if (maxSum < 0)
            return maxSum;
        return Math.max(maxSum, total - minSum);
    }

    // 5. Maximum Product of Three Numbers
    static int maximumProductOfThree(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;

        return Math.max(
                nums[n - 1] * nums[n - 2] * nums[n - 3],
                nums[0] * nums[1] * nums[n - 1]);
    }

    // 6. Partition Array According to Given Pivot
    static int[] pivotArray(int[] nums, int pivot) {
        int[] ans = new int[nums.length];
        int index = 0;

        for (int x : nums)
            if (x < pivot)
                ans[index++] = x;

        for (int x : nums)
            if (x == pivot)
                ans[index++] = x;

        for (int x : nums)
            if (x > pivot)
                ans[index++] = x;

        return ans;
    }

    // 7. Maximum Erasure Value
    static int maximumUniqueSubarray(int[] nums) {
        Set<Integer> set = new HashSet<>();
        int left = 0, sum = 0, ans = 0;

        for (int right = 0; right < nums.length; right++) {
            while (set.contains(nums[right])) {
                set.remove(nums[left]);
                sum -= nums[left++];
            }

            set.add(nums[right]);
            sum += nums[right];
            ans = Math.max(ans, sum);
        }

        return ans;
    }

    // 8. Longest Turbulent Subarray
    static int maxTurbulenceSize(int[] arr) {
        if (arr.length <= 1)
            return arr.length;

        int up = 1, down = 1, ans = 1;

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > arr[i - 1]) {
                up = down + 1;
                down = 1;
            } else if (arr[i] < arr[i - 1]) {
                down = up + 1;
                up = 1;
            } else {
                up = down = 1;
            }
            ans = Math.max(ans, Math.max(up, down));
        }

        return ans;
    }

    // =========================================================
    // SESSION 5 - ARRAY II
    // =========================================================

    // 1. Two Sum
    static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int need = target - nums[i];

            if (map.containsKey(need))
                return new int[] { map.get(need), i };

            map.put(nums[i], i);
        }

        return new int[] { -1, -1 };
    }

    // 2. Count Elements With Maximum Frequency
    static int countMaxFrequency(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        int max = 0;

        for (int x : nums) {
            int f = map.getOrDefault(x, 0) + 1;
            map.put(x, f);
            max = Math.max(max, f);
        }

        int count = 0;
        for (int f : map.values())
            if (f == max)
                count += f;

        return count;
    }

    // 3. Rotate Array Right by k
    static void rotateRight(int[] nums, int k) {
        if (nums == null || nums.length <= 1)
            return;
        k %= nums.length;
        if (k < 0)
            k += nums.length;
        if (k == 0)
            return;
        reverse(nums, 0, nums.length - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.length - 1);
    }

    // 4. Rotate Array Left by k
    static void rotateLeft(int[] nums, int k) {
        if (nums == null || nums.length <= 1)
            return;
        k %= nums.length;
        if (k < 0)
            k += nums.length;
        if (k == 0)
            return;
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.length - 1);
        reverse(nums, 0, nums.length - 1);
    }

    static void reverse(int[] nums, int left, int right) {
        while (left < right) {
            int temp = nums[left];
            nums[left++] = nums[right];
            nums[right--] = temp;
        }
    }

    // 5. Lucky Integer in an Array
    static int findLucky(int[] arr) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int x : arr)
            map.put(x, map.getOrDefault(x, 0) + 1);

        int ans = -1;

        for (int x : map.keySet())
            if (x == map.get(x))
                ans = Math.max(ans, x);

        return ans;
    }

    // 6. Shuffle the Array
    static int[] shuffle(int[] nums, int n) {
        int[] ans = new int[2 * n];
        int index = 0;

        for (int i = 0; i < n; i++) {
            ans[index++] = nums[i];
            ans[index++] = nums[i + n];
        }

        return ans;
    }

    // 7. Can Place Flowers
    static boolean canPlaceFlowers(int[] flowerbed, int n) {
        for (int i = 0; i < flowerbed.length && n > 0; i++) {
            if (flowerbed[i] == 0 &&
                    (i == 0 || flowerbed[i - 1] == 0) &&
                    (i == flowerbed.length - 1 || flowerbed[i + 1] == 0)) {

                flowerbed[i] = 1;
                n--;
            }
        }

        return n == 0;
    }

    // 8. Find All Numbers Disappeared in an Array
    static List<Integer> findDisappearedNumbers(int[] nums) {
        for (int x : nums) {
            int index = Math.abs(x) - 1;
            if (nums[index] > 0)
                nums[index] = -nums[index];
        }

        List<Integer> ans = new ArrayList<>();

        for (int i = 0; i < nums.length; i++)
            if (nums[i] > 0)
                ans.add(i + 1);

        return ans;
    }

    // 9. First Missing Positive
    static int firstMissingPositive(int[] nums) {
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            while (nums[i] >= 1 &&
                    nums[i] <= n &&
                    nums[nums[i] - 1] != nums[i]) {

                int temp = nums[i];
                nums[i] = nums[temp - 1];
                nums[temp - 1] = temp;
            }
        }

        for (int i = 0; i < n; i++)
            if (nums[i] != i + 1)
                return i + 1;

        return n + 1;
    }

    // 10. Pivot Index (also repeated in syllabus)
    // Use pivotIndex() from Session 3.

    // =========================================================
    // SESSION 6 - ARRAY III
    // =========================================================

    // 1. Sort Colors - Dutch National Flag
    static void sortColors(int[] nums) {
        int low = 0, mid = 0, high = nums.length - 1;

        while (mid <= high) {
            if (nums[mid] == 0) {
                swap(nums, low++, mid++);
            } else if (nums[mid] == 1) {
                mid++;
            } else {
                swap(nums, mid, high--);
            }
        }
    }

    static void swap(int[] a, int i, int j) {
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }

    // 2. Container With Most Water
    static int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int ans = 0;

        while (left < right) {
            int area = Math.min(height[left], height[right]) * (right - left);
            ans = Math.max(ans, area);

            if (height[left] < height[right])
                left++;
            else
                right--;
        }

        return ans;
    }

    // 3. Trapping Rain Water
    static int trap(int[] height) {
        int left = 0, right = height.length - 1;
        int leftMax = 0, rightMax = 0;
        int water = 0;

        while (left <= right) {
            if (height[left] <= height[right]) {
                if (height[left] >= leftMax)
                    leftMax = height[left];
                else
                    water += leftMax - height[left];

                left++;
            } else {
                if (height[right] >= rightMax)
                    rightMax = height[right];
                else
                    water += rightMax - height[right];

                right--;
            }
        }

        return water;
    }

    // 4. Height Checker
    static int heightChecker(int[] heights) {
        int[] sorted = heights.clone();
        Arrays.sort(sorted);

        int count = 0;

        for (int i = 0; i < heights.length; i++)
            if (heights[i] != sorted[i])
                count++;

        return count;
    }

    // 5. Squares of a Sorted Array
    static int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];

        int left = 0, right = n - 1;

        for (int i = n - 1; i >= 0; i--) {
            int l = nums[left] * nums[left];
            int r = nums[right] * nums[right];

            if (l > r) {
                ans[i] = l;
                left++;
            } else {
                ans[i] = r;
                right--;
            }
        }

        return ans;
    }

    // 6. Boats to Save People
    static int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);

        int left = 0, right = people.length - 1;
        int boats = 0;

        while (left <= right) {
            if (people[left] + people[right] <= limit)
                left++;

            right--;
            boats++;
        }

        return boats;
    }

    // 7. 3Sum
    static List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> ans = new ArrayList<>();

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1])
                continue;

            int left = i + 1;
            int right = nums.length - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];

                if (sum == 0) {
                    ans.add(Arrays.asList(nums[i], nums[left], nums[right]));

                    while (left < right && nums[left] == nums[left + 1])
                        left++;
                    while (left < right && nums[right] == nums[right - 1])
                        right--;

                    left++;
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return ans;
    }

    // 8. Candy
    static int candy(int[] ratings) {
        int n = ratings.length;
        int[] candies = new int[n];
        Arrays.fill(candies, 1);

        for (int i = 1; i < n; i++)
            if (ratings[i] > ratings[i - 1])
                candies[i] = candies[i - 1] + 1;

        for (int i = n - 2; i >= 0; i--)
            if (ratings[i] > ratings[i + 1])
                candies[i] = Math.max(candies[i], candies[i + 1] + 1);

        int ans = 0;
        for (int x : candies)
            ans += x;

        return ans;
    }

    // 9. Jump Game
    static boolean canJump(int[] nums) {
        int farthest = 0;

        for (int i = 0; i < nums.length; i++) {
            if (i > farthest)
                return false;

            farthest = Math.max(farthest, i + nums[i]);
        }

        return true;
    }

    // =========================================================
    // SESSION 7 - BINARY SEARCH I
    // =========================================================

    // Basic Binary Search
    static int binarySearch(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target)
                return mid;
            if (nums[mid] < target)
                left = mid + 1;
            else
                right = mid - 1;
        }

        return -1;
    }

    // 1. Lower Bound
    static int lowerBound(int[] nums, int target) {
        int left = 0, right = nums.length;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] >= target)
                right = mid;
            else
                left = mid + 1;
        }

        return left;
    }

    // 2. Upper Bound
    static int upperBound(int[] nums, int target) {
        int left = 0, right = nums.length;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] > target)
                right = mid;
            else
                left = mid + 1;
        }

        return left;
    }

    // 3. Koko Eating Bananas
    static int minEatingSpeed(int[] piles, int h) {
        int low = 1;
        int high = 0;

        for (int x : piles)
            high = Math.max(high, x);

        while (low < high) {
            int mid = low + (high - low) / 2;

            if (canEat(piles, h, mid))
                high = mid;
            else
                low = mid + 1;
        }

        return low;
    }

    static boolean canEat(int[] piles, int h, int speed) {
        long hours = 0;

        for (int x : piles) {
            hours += (x + speed - 1L) / speed;
            if (hours > h)
                return false;
        }

        return true;
    }

    // 4. First Bad Version
    // Replace isBadVersion() with the API supplied by LeetCode.
    static int firstBadVersion(int n) {
        int left = 1, right = n;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (isBadVersion(mid))
                right = mid;
            else
                left = mid + 1;
        }

        return left;
    }

    static boolean isBadVersion(int version) {
        // Example placeholder.
        // In LeetCode this method is supplied by the system.
        return false;
    }

    // 5. Search Insert Position
    static int searchInsert(int[] nums, int target) {
        int left = 0, right = nums.length;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] < target)
                left = mid + 1;
            else
                right = mid;
        }

        return left;
    }

    // 6. Arranging Coins
    static int arrangeCoins(int n) {
        long left = 0, right = n;

        while (left <= right) {
            long mid = left + (right - left) / 2;
            long coins = mid * (mid + 1) / 2;

            if (coins == n)
                return (int) mid;

            if (coins < n)
                left = mid + 1;
            else
                right = mid - 1;
        }

        return (int) right;
    }

    // 7. Find Smallest Letter Greater Than Target
    static char nextGreatestLetter(char[] letters, char target) {
        int left = 0, right = letters.length;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (letters[mid] <= target)
                left = mid + 1;
            else
                right = mid;
        }

        return letters[left % letters.length];
    }

    // 8. Find Peak Element
    static int findPeakElement(int[] nums) {
        int left = 0, right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] > nums[mid + 1])
                right = mid;
            else
                left = mid + 1;
        }

        return left;
    }

    // 9. First and Last Position of Element
    static int[] searchRange(int[] nums, int target) {
        int first = lowerBound(nums, target);

        if (first == nums.length || nums[first] != target)
            return new int[] { -1, -1 };

        int last = upperBound(nums, target) - 1;

        return new int[] { first, last };
    }

    // =========================================================
    // SESSION 8 - BINARY SEARCH II
    // =========================================================

    // 1. Search in Rotated Sorted Array
    static int searchRotated(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target)
                return mid;

            if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid])
                    right = mid - 1;
                else
                    left = mid + 1;
            } else {
                if (nums[mid] < target && target <= nums[right])
                    left = mid + 1;
                else
                    right = mid - 1;
            }
        }

        return -1;
    }

    // 2. Find Minimum in Rotated Sorted Array
    static int findMinRotated(int[] nums) {
        int left = 0, right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] > nums[right])
                left = mid + 1;
            else
                right = mid;
        }

        return nums[left];
    }

    // 3. Peak Index in a Mountain Array
    static int peakIndexInMountainArray(int[] arr) {
        int left = 0, right = arr.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (arr[mid] < arr[mid + 1])
                left = mid + 1;
            else
                right = mid;
        }

        return left;
    }

    // 4. Find in Mountain Array
    // Standard version when the full array is available.
    static int findInMountainArray(int target, int[] arr) {
        int peak = peakIndexInMountainArray(arr);

        int leftResult = binarySearchAscending(arr, target, 0, peak);
        if (leftResult != -1)
            return leftResult;

        return binarySearchDescending(arr, target, peak + 1, arr.length - 1);
    }

    static int binarySearchAscending(int[] a, int target, int left, int right) {
        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (a[mid] == target)
                return mid;
            if (a[mid] < target)
                left = mid + 1;
            else
                right = mid - 1;
        }
        return -1;
    }

    static int binarySearchDescending(int[] a, int target, int left, int right) {
        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (a[mid] == target)
                return mid;
            if (a[mid] > target)
                left = mid + 1;
            else
                right = mid - 1;
        }
        return -1;
    }

    // 5. Magnetic Force Between Two Balls
    static int maxDistance(int[] position, int m) {
        Arrays.sort(position);

        int low = 1;
        int high = position[position.length - 1] - position[0];

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (canPlaceBalls(position, m, mid))
                low = mid + 1;
            else
                high = mid - 1;
        }

        return high;
    }

    static boolean canPlaceBalls(int[] position, int m, int distance) {
        int count = 1;
        int last = position[0];

        for (int i = 1; i < position.length; i++) {
            if (position[i] - last >= distance) {
                count++;
                last = position[i];
            }
        }

        return count >= m;
    }

    // 6. Capacity to Ship Packages Within D Days
    static int shipWithinDays(int[] weights, int days) {
        int low = 0;
        int high = 0;

        for (int x : weights) {
            low = Math.max(low, x);
            high += x;
        }

        while (low < high) {
            int mid = low + (high - low) / 2;

            if (canShip(weights, days, mid))
                high = mid;
            else
                low = mid + 1;
        }

        return low;
    }

    static boolean canShip(int[] weights, int days, int capacity) {
        int usedDays = 1;
        int current = 0;

        for (int x : weights) {
            if (current + x > capacity) {
                usedDays++;
                current = 0;
            }

            current += x;
        }

        return usedDays <= days;
    }

    // =========================================================
    // SESSION 9 - MATRIX PROBLEMS I
    // =========================================================

    // 1. Spiral Traversal
    static List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> ans = new ArrayList<>();

        if (matrix.length == 0)
            return ans;

        int top = 0, bottom = matrix.length - 1;
        int left = 0, right = matrix[0].length - 1;

        while (top <= bottom && left <= right) {
            for (int j = left; j <= right; j++)
                ans.add(matrix[top][j]);
            top++;

            for (int i = top; i <= bottom; i++)
                ans.add(matrix[i][right]);
            right--;

            if (top <= bottom) {
                for (int j = right; j >= left; j--)
                    ans.add(matrix[bottom][j]);
                bottom--;
            }

            if (left <= right) {
                for (int i = bottom; i >= top; i--)
                    ans.add(matrix[i][left]);
                left++;
            }
        }

        return ans;
    }

    // 2. Search a 2D Matrix
    static boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0 || matrix[0].length == 0)
            return false;

        int rows = matrix.length;
        int cols = matrix[0].length;

        int left = 0;
        int right = rows * cols - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            int value = matrix[mid / cols][mid % cols];

            if (value == target)
                return true;
            if (value < target)
                left = mid + 1;
            else
                right = mid - 1;
        }

        return false;
    }

    // 3. Print Matrix Elements in Sorted Order
    static List<Integer> sortedMatrixElements(int[][] matrix) {
        List<Integer> ans = new ArrayList<>();

        for (int[] row : matrix)
            for (int x : row)
                ans.add(x);

        Collections.sort(ans);
        return ans;
    }

    // =========================================================
    // SESSION 10 - MATRIX PROBLEMS II
    // =========================================================

    // 1. Matrix Diagonal Sum
    static int diagonalSum(int[][] mat) {
        int n = mat.length;
        int sum = 0;

        for (int i = 0; i < n; i++) {
            sum += mat[i][i];
            sum += mat[i][n - 1 - i];
        }

        if (n % 2 == 1)
            sum -= mat[n / 2][n / 2];

        return sum;
    }

    // 2. Reshape the Matrix
    static int[][] matrixReshape(int[][] mat, int r, int c) {
        int oldR = mat.length;
        int oldC = mat[0].length;

        if (oldR * oldC != r * c)
            return mat;

        int[][] ans = new int[r][c];

        for (int i = 0; i < oldR * oldC; i++)
            ans[i / c][i % c] = mat[i / oldC][i % oldC];

        return ans;
    }

    // 3. Toeplitz Matrix
    static boolean isToeplitzMatrix(int[][] matrix) {
        for (int i = 1; i < matrix.length; i++)
            for (int j = 1; j < matrix[0].length; j++)
                if (matrix[i][j] != matrix[i - 1][j - 1])
                    return false;

        return true;
    }

    // 4. Diagonal Traverse
    static int[] findDiagonalOrder(int[][] mat) {
        int rows = mat.length;
        int cols = mat[0].length;

        int[] ans = new int[rows * cols];
        int index = 0;

        for (int d = 0; d < rows + cols - 1; d++) {
            List<Integer> temp = new ArrayList<>();

            int row = d < cols ? 0 : d - cols + 1;
            int col = d < cols ? d : cols - 1;

            while (row < rows && col >= 0) {
                temp.add(mat[row][col]);
                row++;
                col--;
            }

            if (d % 2 == 0)
                Collections.reverse(temp);

            for (int x : temp)
                ans[index++] = x;
        }

        return ans;
    }

    // 5. Spiral Matrix
    // Same standard solution as spiralOrder().
    // Use spiralOrder(matrix).

    // 6. Search a 2D Matrix II
    static boolean searchMatrixII(int[][] matrix, int target) {
        if (matrix.length == 0)
            return false;

        int row = 0;
        int col = matrix[0].length - 1;

        while (row < matrix.length && col >= 0) {
            if (matrix[row][col] == target)
                return true;

            if (matrix[row][col] > target)
                col--;
            else
                row++;
        }

        return false;
    }

    // 7. Median in Row-Wise Sorted Matrix
    static int matrixMedian(int[][] matrix) {
        int low = Integer.MAX_VALUE;
        int high = Integer.MIN_VALUE;

        for (int[] row : matrix) {
            low = Math.min(low, row[0]);
            high = Math.max(high, row[row.length - 1]);
        }

        int desired = (matrix.length * matrix[0].length + 1) / 2;

        while (low < high) {
            int mid = low + (high - low) / 2;
            int count = 0;

            for (int[] row : matrix)
                count += upperBound(row, mid);

            if (count < desired)
                low = mid + 1;
            else
                high = mid;
        }

        return low;
    }

    // 8. Row With Maximum Number of 1s
    static int rowWithMaxOnes(int[][] mat) {
        int row = -1;
        int maxOnes = 0;

        for (int i = 0; i < mat.length; i++) {
            int firstOne = lowerBound(mat[i], 1);
            int ones = mat[i].length - firstOne;

            if (ones > maxOnes) {
                maxOnes = ones;
                row = i;
            }
        }

        return row;
    }

    // 9. Rotate Image 90 Degrees Clockwise
    static void rotateImage(int[][] matrix) {
        int n = matrix.length;

        // Transpose
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        // Reverse every row
        for (int[] row : matrix) {
            int left = 0, right = n - 1;

            while (left < right) {
                int temp = row[left];
                row[left++] = row[right];
                row[right--] = temp;
            }
        }
    }

    // 10. Flipping an Image
    static int[][] flipAndInvertImage(int[][] image) {
        for (int[] row : image) {
            int left = 0, right = row.length - 1;

            while (left <= right) {
                int temp = row[left] ^ 1;
                row[left] = row[right] ^ 1;
                row[right] = temp;

                left++;
                right--;
            }
        }

        return image;
    }

    // 11. Count Negative Numbers in a Sorted Matrix
    static int countNegatives(int[][] grid) {
        int count = 0;

        for (int[] row : grid) {
            int left = 0, right = row.length;

            while (left < right) {
                int mid = left + (right - left) / 2;

                if (row[mid] < 0)
                    right = mid;
                else
                    left = mid + 1;
            }

            count += row.length - left;
        }

        return count;
    }

    // 12. Image Smoother
    static int[][] imageSmoother(int[][] img) {
        int rows = img.length;
        int cols = img[0].length;
        int[][] ans = new int[rows][cols];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                int sum = 0, count = 0;

                for (int x = i - 1; x <= i + 1; x++) {
                    for (int y = j - 1; y <= j + 1; y++) {
                        if (x >= 0 && x < rows && y >= 0 && y < cols) {
                            sum += img[x][y];
                            count++;
                        }
                    }
                }

                ans[i][j] = sum / count;
            }
        }

        return ans;
    }

    // 13. Diagonal Sort
    static int[][] diagonalSort(int[][] mat) {
        int rows = mat.length;
        int cols = mat[0].length;

        // Diagonals starting from first row
        for (int startCol = 0; startCol < cols; startCol++)
            sortDiagonal(mat, 0, startCol);

        // Diagonals starting from first column
        for (int startRow = 1; startRow < rows; startRow++)
            sortDiagonal(mat, startRow, 0);

        return mat;
    }

    static void sortDiagonal(int[][] mat, int row, int col) {
        List<Integer> list = new ArrayList<>();

        int i = row, j = col;

        while (i < mat.length && j < mat[0].length) {
            list.add(mat[i][j]);
            i++;
            j++;
        }

        Collections.sort(list);

        i = row;
        j = col;
        int index = 0;

        while (i < mat.length && j < mat[0].length) {
            mat[i][j] = list.get(index++);
            i++;
            j++;
        }
    }

    // 14. Game of Life
    static void gameOfLife(int[][] board) {
        int rows = board.length;
        int cols = board[0].length;

        int[] dr = { -1, -1, -1, 0, 0, 1, 1, 1 };
        int[] dc = { -1, 0, 1, -1, 1, -1, 0, 1 };

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                int live = 0;

                for (int k = 0; k < 8; k++) {
                    int nr = r + dr[k];
                    int nc = c + dc[k];

                    if (nr >= 0 && nr < rows &&
                            nc >= 0 && nc < cols &&
                            Math.abs(board[nr][nc]) == 1) {
                        live++;
                    }
                }

                if (board[r][c] == 1 && (live < 2 || live > 3))
                    board[r][c] = -1;

                if (board[r][c] == 0 && live == 3)
                    board[r][c] = 2;
            }
        }

        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                if (board[r][c] == -1)
                    board[r][c] = 0;
                else if (board[r][c] == 2)
                    board[r][c] = 1;
    }

    // =========================================================
    // SESSION 11 - STRINGS I
    // =========================================================

    // 1. Frequency of a Character
    static int characterFrequency(String s, char ch) {
        int count = 0;

        for (char c : s.toCharArray())
            if (c == ch)
                count++;

        return count;
    }

    // 2. Count Number of Words in a String
    static int countWords(String s) {
        s = s.trim();

        if (s.isEmpty())
            return 0;

        return s.split("\\s+").length;
    }

    // 3. Isomorphic Strings
    static boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length())
            return false;

        int[] mapST = new int[256];
        int[] mapTS = new int[256];

        Arrays.fill(mapST, -1);
        Arrays.fill(mapTS, -1);

        for (int i = 0; i < s.length(); i++) {
            int a = s.charAt(i);
            int b = t.charAt(i);

            if (mapST[a] == -1 && mapTS[b] == -1) {
                mapST[a] = b;
                mapTS[b] = a;
            } else if (mapST[a] != b || mapTS[b] != a) {
                return false;
            }
        }

        return true;
    }

    // 4. To Lower Case
    static String toLowerCaseSimple(String s) {
        return s.toLowerCase();
    }

    // 5. Reverse String II
    static String reverseStr(String s, int k) {
        char[] a = s.toCharArray();

        for (int start = 0; start < a.length; start += 2 * k) {
            int left = start;
            int right = Math.min(start + k - 1, a.length - 1);

            while (left < right) {
                char temp = a[left];
                a[left++] = a[right];
                a[right--] = temp;
            }
        }

        return new String(a);
    }

    // 6. Find the Difference
    static char findTheDifference(String s, String t) {
        int result = 0;

        for (char c : s.toCharArray())
            result ^= c;
        for (char c : t.toCharArray())
            result ^= c;

        return (char) result;
    }

    // 7. Ransom Note
    static boolean canConstruct(String ransomNote, String magazine) {
        int[] freq = new int[26];

        for (char c : magazine.toCharArray())
            freq[c - 'a']++;

        for (char c : ransomNote.toCharArray()) {
            if (--freq[c - 'a'] < 0)
                return false;
        }

        return true;
    }

    // 8. Word Pattern
    static boolean wordPattern(String pattern, String s) {
        String[] words = s.split(" ");

        if (words.length != pattern.length())
            return false;

        Map<Character, String> map = new HashMap<>();
        Set<String> used = new HashSet<>();

        for (int i = 0; i < pattern.length(); i++) {
            char ch = pattern.charAt(i);

            if (map.containsKey(ch)) {
                if (!map.get(ch).equals(words[i]))
                    return false;
            } else {
                if (used.contains(words[i]))
                    return false;

                map.put(ch, words[i]);
                used.add(words[i]);
            }
        }

        return true;
    }

    // 9. Check if One String Swap Can Make Strings Equal
    static boolean areAlmostEqual(String s1, String s2) {
        if (s1.equals(s2))
            return true;
        if (s1.length() != s2.length())
            return false;

        List<Integer> diff = new ArrayList<>();

        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i))
                diff.add(i);
        }

        if (diff.size() != 2)
            return false;

        int a = diff.get(0);
        int b = diff.get(1);

        return s1.charAt(a) == s2.charAt(b) &&
                s1.charAt(b) == s2.charAt(a);
    }

    // =========================================================
    // SESSION 12 - STRINGS II
    // =========================================================

    // 1. Valid Anagram
    static boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;

        int[] freq = new int[26];

        for (char c : s.toCharArray())
            freq[c - 'a']++;
        for (char c : t.toCharArray())
            freq[c - 'a']--;

        for (int x : freq)
            if (x != 0)
                return false;

        return true;
    }

    // 2. Longest Common Prefix
    static String longestCommonPrefix(String[] strs) {
        if (strs.length == 0)
            return "";

        String prefix = strs[0];

        for (int i = 1; i < strs.length; i++) {
            while (!strs[i].startsWith(prefix)) {
                prefix = prefix.substring(0, prefix.length() - 1);

                if (prefix.isEmpty())
                    return "";
            }
        }

        return prefix;
    }

    // 3. Minimum Repetition to Make Substring
    static int minRepeats(String a, String b) {
        if (a == null || b == null)
            return -1;
        if (b.isEmpty())
            return 0;
        if (a.isEmpty())
            return -1;

        StringBuilder sb = new StringBuilder();
        int count = 0;

        while (sb.length() < b.length()) {
            sb.append(a);
            count++;
        }

        if (sb.indexOf(b) != -1)
            return count;

        sb.append(a);
        count++;

        if (sb.indexOf(b) != -1)
            return count;

        return -1;
    }

    // 4. Valid Palindrome
    static boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;

        while (left < right) {
            while (left < right && !Character.isLetterOrDigit(s.charAt(left)))
                left++;

            while (left < right && !Character.isLetterOrDigit(s.charAt(right)))
                right--;

            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right)))
                return false;

            left++;
            right--;
        }

        return true;
    }

    // 5. Reverse Words in a String III
    static String reverseWords(String s) {
        String[] words = s.split(" ");
        StringBuilder ans = new StringBuilder();

        for (int i = 0; i < words.length; i++) {
            StringBuilder word = new StringBuilder(words[i]).reverse();

            if (i > 0)
                ans.append(" ");
            ans.append(word);
        }

        return ans.toString();
    }

    // 6. Repeated Substring Pattern
    static boolean repeatedSubstringPattern(String s) {
        String doubled = s + s;
        return doubled.substring(1, doubled.length() - 1).contains(s);
    }

    // 7. Implement strStr / indexOf using KMP
    static int strStr(String haystack, String needle) {
        if (needle.isEmpty())
            return 0;

        int[] lps = buildLPS(needle);
        int i = 0, j = 0;

        while (i < haystack.length()) {
            if (haystack.charAt(i) == needle.charAt(j)) {
                i++;
                j++;

                if (j == needle.length())
                    return i - j;
            } else if (j > 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }

        return -1;
    }

    static int[] buildLPS(String pattern) {
        int[] lps = new int[pattern.length()];
        int len = 0;
        int i = 1;

        while (i < pattern.length()) {
            if (pattern.charAt(i) == pattern.charAt(len)) {
                lps[i++] = ++len;
            } else if (len > 0) {
                len = lps[len - 1];
            } else {
                lps[i++] = 0;
            }
        }

        return lps;
    }

    // 8. Longest Happy Prefix
    static String longestPrefix(String s) {
        if (s == null || s.length() <= 1)
            return "";
        int[] lps = buildLPS(s);
        return s.substring(0, lps[s.length() - 1]);
    }

    // 9. Longest Prefix/Suffix helper
    static String longestPrefixSuffix(String s) {
        return longestPrefix(s);
    }

    // =========================================================
    // SESSION 13-15 - LINKED LIST
    // =========================================================

    static class ListNode {
        int val;
        ListNode next;

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    // 1. Add Node at any position
    static ListNode insertAtPosition(ListNode head, int value, int position) {
        if (position < 0)
            return head;

        ListNode newNode = new ListNode(value);

        if (position == 0) {
            newNode.next = head;
            return newNode;
        }

        ListNode cur = head;

        for (int i = 0; i < position - 1 && cur != null; i++)
            cur = cur.next;

        if (cur == null)
            return head;

        newNode.next = cur.next;
        cur.next = newNode;

        return head;
    }

    // 2. Delete Node from given position
    static ListNode deleteAtPosition(ListNode head, int position) {
        if (head == null || position < 0)
            return head;

        if (position == 0)
            return head.next;

        ListNode cur = head;

        for (int i = 0; i < position - 1 && cur.next != null; i++)
            cur = cur.next;

        if (cur.next != null)
            cur.next = cur.next.next;

        return head;
    }

    // 3. Search Node
    static int searchNode(ListNode head, int target) {
        int index = 0;

        while (head != null) {
            if (head.val == target)
                return index;

            head = head.next;
            index++;
        }

        return -1;
    }

    // 4. Count Nodes
    static int countNodes(ListNode head) {
        int count = 0;

        while (head != null) {
            count++;
            head = head.next;
        }

        return count;
    }

    // 5. Linked List Cycle
    static boolean hasCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast)
                return true;
        }

        return false;
    }

    // 6. Remove Linked List Elements
    static ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode(0, head);
        ListNode cur = dummy;

        while (cur.next != null) {
            if (cur.next.val == val)
                cur.next = cur.next.next;
            else
                cur = cur.next;
        }

        return dummy.next;
    }

    // 7. Remove Duplicates from Sorted List
    static ListNode deleteDuplicates(ListNode head) {
        ListNode cur = head;

        while (cur != null && cur.next != null) {
            if (cur.val == cur.next.val)
                cur.next = cur.next.next;
            else
                cur = cur.next;
        }

        return head;
    }

    // 8. Intersection of Two Linked Lists
    static ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode a = headA;
        ListNode b = headB;

        while (a != b) {
            a = (a == null) ? headB : a.next;
            b = (b == null) ? headA : b.next;
        }

        return a;
    }

    // 9. Remove Zero Sum Consecutive Nodes
    static ListNode removeZeroSumSublists(ListNode head) {
        ListNode dummy = new ListNode(0, head);

        Map<Integer, ListNode> map = new HashMap<>();
        int sum = 0;

        for (ListNode cur = dummy; cur != null; cur = cur.next) {
            sum += cur.val;
            map.put(sum, cur);
        }

        sum = 0;

        for (ListNode cur = dummy; cur != null; cur = cur.next) {
            sum += cur.val;
            cur.next = map.get(sum).next;
        }

        return dummy.next;
    }

    // 10. Split Linked List in Parts
    static ListNode[] splitListToParts(ListNode root, int k) {
        int length = countNodes(root);

        ListNode[] ans = new ListNode[k];

        int base = length / k;
        int extra = length % k;

        ListNode cur = root;

        for (int i = 0; i < k; i++) {
            ans[i] = cur;

            int size = base + (i < extra ? 1 : 0);

            for (int j = 1; j < size && cur != null; j++)
                cur = cur.next;

            if (cur != null) {
                ListNode next = cur.next;
                cur.next = null;
                cur = next;
            }
        }

        return ans;
    }

    // 11. Reverse Linked List
    static ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode cur = head;

        while (cur != null) {
            ListNode next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }

        return prev;
    }

    // 12. Middle of Linked List
    static ListNode middleNode(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        return slow;
    }

    // 13. Merge Two Sorted Linked Lists
    static ListNode mergeTwoLists(ListNode a, ListNode b) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;

        while (a != null && b != null) {
            if (a.val <= b.val) {
                cur.next = a;
                a = a.next;
            } else {
                cur.next = b;
                b = b.next;
            }

            cur = cur.next;
        }

        cur.next = (a != null) ? a : b;

        return dummy.next;
    }

    // 14. Reverse Nodes in Even Length Groups
    static ListNode reverseEvenLengthGroups(ListNode head) {
        ListNode dummy = new ListNode(0, head);
        ListNode prev = dummy;
        int groupSize = 1;

        while (prev.next != null) {
            ListNode groupStart = prev.next;
            ListNode node = groupStart;
            int count = 0;

            while (node != null && count < groupSize) {
                node = node.next;
                count++;
            }

            if (count % 2 == 0) {
                ListNode cur = groupStart;
                ListNode before = prev;

                for (int i = 0; i < count; i++) {
                    ListNode next = cur.next;
                    cur.next = before;
                    before = cur;
                    cur = next;
                }

                ListNode oldStart = groupStart;
                oldStart.next = cur;
                prev.next = before;
                prev = oldStart;
            } else {
                for (int i = 0; i < count; i++)
                    prev = prev.next;
            }

            groupSize++;
        }

        return dummy.next;
    }

    // 15. Swap Nodes in Pairs
    static ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0, head);
        ListNode prev = dummy;

        while (prev.next != null && prev.next.next != null) {
            ListNode first = prev.next;
            ListNode second = first.next;

            first.next = second.next;
            second.next = first;
            prev.next = second;

            prev = first;
        }

        return dummy.next;
    }

    // 16. Reverse Linked List II
    static ListNode reverseBetween(ListNode head, int left, int right) {
        if (head == null || left == right)
            return head;

        ListNode dummy = new ListNode(0, head);
        ListNode prev = dummy;

        for (int i = 1; i < left; i++)
            prev = prev.next;

        ListNode cur = prev.next;

        for (int i = 0; i < right - left; i++) {
            ListNode move = cur.next;
            cur.next = move.next;
            move.next = prev.next;
            prev.next = move;
        }

        return dummy.next;
    }

    // 17. Maximum Twin Sum of a Linked List
    static int pairSum(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode second = reverseList(slow);
        ListNode first = head;

        int ans = 0;

        while (second != null) {
            ans = Math.max(ans, first.val + second.val);
            first = first.next;
            second = second.next;
        }

        return ans;
    }

    // 18. Add Two Numbers
    static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;

        int carry = 0;

        while (l1 != null || l2 != null || carry != 0) {
            int sum = carry;

            if (l1 != null) {
                sum += l1.val;
                l1 = l1.next;
            }

            if (l2 != null) {
                sum += l2.val;
                l2 = l2.next;
            }

            cur.next = new ListNode(sum % 10);
            cur = cur.next;
            carry = sum / 10;
        }

        return dummy.next;
    }

    // 19. Rotate List
    static ListNode rotateRightList(ListNode head, int k) {
        if (head == null || head.next == null || k == 0)
            return head;

        int length = 1;
        ListNode tail = head;

        while (tail.next != null) {
            tail = tail.next;
            length++;
        }

        k %= length;
        if (k == 0)
            return head;

        tail.next = head;

        int steps = length - k;
        ListNode newTail = tail;

        while (steps-- > 0)
            newTail = newTail.next;

        ListNode newHead = newTail.next;
        newTail.next = null;

        return newHead;
    }

    // 20. Delete Middle Node
    static ListNode deleteMiddle(ListNode head) {
        if (head == null || head.next == null)
            return null;

        ListNode slow = head;
        ListNode fast = head;
        ListNode prev = null;

        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }

        prev.next = slow.next;

        return head;
    }

    // 21. Partition List
    static ListNode partition(ListNode head, int x) {
        ListNode before = new ListNode(0);
        ListNode after = new ListNode(0);

        ListNode b = before;
        ListNode a = after;

        while (head != null) {
            if (head.val < x) {
                b.next = head;
                b = b.next;
            } else {
                a.next = head;
                a = a.next;
            }

            head = head.next;
        }

        a.next = null;
        b.next = after.next;

        return before.next;
    }

    // 22. Odd Even Linked List
    static ListNode oddEvenList(ListNode head) {
        if (head == null)
            return null;

        ListNode odd = head;
        ListNode even = head.next;
        ListNode evenHead = even;

        while (even != null && even.next != null) {
            odd.next = even.next;
            odd = odd.next;

            even.next = odd.next;
            even = even.next;
        }

        odd.next = evenHead;

        return head;
    }

    // 23. Reorder List
    static void reorderList(ListNode head) {
        if (head == null || head.next == null)
            return;

        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode second = reverseList(slow);
        ListNode first = head;

        while (second.next != null) {
            ListNode fNext = first.next;
            ListNode sNext = second.next;

            first.next = second;
            second.next = fNext;

            first = fNext;
            second = sNext;
        }
    }

    // 24. Sort List - Merge Sort
    static ListNode sortList(ListNode head) {
        if (head == null || head.next == null)
            return head;

        ListNode slow = head;
        ListNode fast = head.next;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        ListNode second = slow.next;
        slow.next = null;

        ListNode left = sortList(head);
        ListNode right = sortList(second);

        return mergeTwoLists(left, right);
    }

    // 25. Double a Number Represented as a Linked List
    static ListNode doubleIt(ListNode head) {
        head = reverseList(head);

        ListNode cur = head;
        int carry = 0;

        while (cur != null) {
            int value = cur.val * 2 + carry;
            cur.val = value % 10;
            carry = value / 10;

            if (cur.next == null && carry > 0)
                cur.next = new ListNode(carry);

            cur = cur.next;
        }

        return reverseList(head);
    }

    // =========================================================
    // COPY LIST WITH RANDOM POINTER
    // =========================================================

    static class RandomNode {
        int val;
        RandomNode next;
        RandomNode random;

        RandomNode(int val) {
            this.val = val;
        }
    }

    static RandomNode copyRandomList(RandomNode head) {
        if (head == null)
            return null;

        RandomNode cur = head;

        // Insert copy after each original node
        while (cur != null) {
            RandomNode copy = new RandomNode(cur.val);
            copy.next = cur.next;
            cur.next = copy;
            cur = copy.next;
        }

        // Set random pointers
        cur = head;

        while (cur != null) {
            if (cur.random != null)
                cur.next.random = cur.random.next;

            cur = cur.next.next;
        }

        // Separate lists
        RandomNode dummy = new RandomNode(0);
        RandomNode copyCur = dummy;
        cur = head;

        while (cur != null) {
            RandomNode copy = cur.next;

            cur.next = copy.next;
            copyCur.next = copy;
            copyCur = copy;

            cur = cur.next;
        }

        return dummy.next;
    }

    // =========================================================
    // HELPER - PRINT ARRAY
    // =========================================================

    static void printArray(int[] a) {
        System.out.println(Arrays.toString(a));
    }

    static void printList(ListNode head) {
        while (head != null) {
            System.out.print(head.val);

            if (head.next != null)
                System.out.print(" -> ");

            head = head.next;
        }

        System.out.println();
    }

    // =========================================================
    // SAMPLE MAIN
    // =========================================================

    public static void main(String[] args) {
        System.out.println("==================================================");
        System.out.println("  COMPETITIVE CODING CODE BANK - TEST SUITE");
        System.out.println("==================================================");

        // Session 1: Basic Java
        System.out.println("\n--- [Session 1: Basic Java] ---");
        System.out.println("factorialLoop(5) = " + factorialLoop(5) + " (Expected: 120)");
        System.out.println("arraySum([1,2,3,4,5]) = " + arraySum(new int[]{1, 2, 3, 4, 5}) + " (Expected: 15)");
        System.out.println("findMaximum([3,7,2,9,5]) = " + findMaximum(new int[]{3, 7, 2, 9, 5}) + " (Expected: 9)");

        // Session 2: Recursion
        System.out.println("\n--- [Session 2: Recursion] ---");
        System.out.println("factorial(5) = " + factorial(5) + " (Expected: 120)");
        System.out.println("power(2, 5) = " + power(2, 5) + " (Expected: 32)");
        System.out.println("sumDigits(12345) = " + sumDigits(12345) + " (Expected: 15)");
        System.out.println("reverseString(\"hello\") = " + reverseString("hello") + " (Expected: olleh)");
        System.out.println("generateParenthesis(3) = " + generateParenthesis(3));
        System.out.println("expressionAddOperators(\"232\", 8) = " + expressionAddOperators("232", 8));

        // Session 3: Recursion II
        System.out.println("\n--- [Session 3: Recursion II] ---");
        System.out.println("fibonacci(6) = " + fibonacci(6) + " (Expected: 8)");
        System.out.println("pivotIndex([1,7,3,6,5,6]) = " + pivotIndex(new int[]{1, 7, 3, 6, 5, 6}) + " (Expected: 3)");
        System.out.println("removeDuplicates([1,1,2,2,3]) = " + removeDuplicates(new int[]{1, 1, 2, 2, 3}) + " (Expected: 3)");
        System.out.println("getRow(4) (Pascal Row 4) = " + getRow(4) + " (Expected: [1, 4, 6, 4, 1])");
        System.out.println("myPow(2.0, 10) = " + myPow(2.0, 10) + " (Expected: 1024.0)");
        System.out.println("letterTilePossibilities(\"AAB\") = " + letterTilePossibilities("AAB") + " (Expected: 8)");
        System.out.println("kthGrammar(4, 5) = " + kthGrammar(4, 5) + " (Expected: 1)");

        // Session 4: Array I
        System.out.println("\n--- [Session 4: Array I] ---");
        int[] a4 = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        System.out.println("maxSubArray = " + maxSubArray(a4) + " (Expected: 6)");
        System.out.println("maxProduct([2,3,-2,4]) = " + maxProduct(new int[]{2, 3, -2, 4}) + " (Expected: 6)");
        System.out.println("findMaxAverage([1,12,-5,-6,50,3], 4) = " + findMaxAverage(new int[]{1, 12, -5, -6, 50, 3}, 4) + " (Expected: 12.75)");
        System.out.println("maxSubarraySumCircular([1,-2,3,-2]) = " + maxSubarraySumCircular(new int[]{1, -2, 3, -2}) + " (Expected: 3)");
        System.out.println("maximumProductOfThree([-10,-10,5,2]) = " + maximumProductOfThree(new int[]{-10, -10, 5, 2}) + " (Expected: 500)");
        System.out.println("pivotArray([9,12,5,10,14,3,10], 10) = " + Arrays.toString(pivotArray(new int[]{9, 12, 5, 10, 14, 3, 10}, 10)));
        System.out.println("maximumUniqueSubarray([4,2,4,5,6]) = " + maximumUniqueSubarray(new int[]{4, 2, 4, 5, 6}) + " (Expected: 17)");
        System.out.println("maxTurbulenceSize([9,4,2,10,7,8,8,1,9]) = " + maxTurbulenceSize(new int[]{9, 4, 2, 10, 7, 8, 8, 1, 9}) + " (Expected: 5)");

        // Session 5: Array II
        System.out.println("\n--- [Session 5: Array II] ---");
        System.out.println("twoSum([2,7,11,15], 9) = " + Arrays.toString(twoSum(new int[]{2, 7, 11, 15}, 9)) + " (Expected: [0, 1])");
        System.out.println("countMaxFrequency([1,2,2,3,1,4]) = " + countMaxFrequency(new int[]{1, 2, 2, 3, 1, 4}) + " (Expected: 4)");
        int[] rot = {1, 2, 3, 4, 5, 6, 7};
        rotateRight(rot, 3);
        System.out.println("rotateRight([1..7], 3) = " + Arrays.toString(rot) + " (Expected: [5, 6, 7, 1, 2, 3, 4])");
        rotateLeft(rot, 3);
        System.out.println("rotateLeft back = " + Arrays.toString(rot) + " (Expected: [1, 2, 3, 4, 5, 6, 7])");
        System.out.println("findLucky([2,2,3,4]) = " + findLucky(new int[]{2, 2, 3, 4}) + " (Expected: 2)");
        System.out.println("shuffle([2,5,1,3,4,7], 3) = " + Arrays.toString(shuffle(new int[]{2, 5, 1, 3, 4, 7}, 3)));
        System.out.println("canPlaceFlowers([1,0,0,0,1], 1) = " + canPlaceFlowers(new int[]{1, 0, 0, 0, 1}, 1) + " (Expected: true)");
        System.out.println("findDisappearedNumbers([4,3,2,7,8,2,3,1]) = " + findDisappearedNumbers(new int[]{4, 3, 2, 7, 8, 2, 3, 1}) + " (Expected: [5, 6])");
        System.out.println("firstMissingPositive([3,4,-1,1]) = " + firstMissingPositive(new int[]{3, 4, -1, 1}) + " (Expected: 2)");

        // Session 6: Array III
        System.out.println("\n--- [Session 6: Array III] ---");
        int[] col = {2, 0, 2, 1, 1, 0};
        sortColors(col);
        System.out.println("sortColors([2,0,2,1,1,0]) = " + Arrays.toString(col) + " (Expected: [0, 0, 1, 1, 2, 2])");
        System.out.println("maxArea([1,8,6,2,5,4,8,3,7]) = " + maxArea(new int[]{1, 8, 6, 2, 5, 4, 8, 3, 7}) + " (Expected: 49)");
        System.out.println("trap([0,1,0,2,1,0,1,3,2,1,2,1]) = " + trap(new int[]{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}) + " (Expected: 6)");
        System.out.println("heightChecker([1,1,4,2,1,3]) = " + heightChecker(new int[]{1, 1, 4, 2, 1, 3}) + " (Expected: 3)");
        System.out.println("sortedSquares([-4,-1,0,3,10]) = " + Arrays.toString(sortedSquares(new int[]{-4, -1, 0, 3, 10})));
        System.out.println("numRescueBoats([3,2,2,1], 3) = " + numRescueBoats(new int[]{3, 2, 2, 1}, 3) + " (Expected: 3)");
        System.out.println("threeSum([-1,0,1,2,-1,-4]) = " + threeSum(new int[]{-1, 0, 1, 2, -1, -4}));
        System.out.println("candy([1,0,2]) = " + candy(new int[]{1, 0, 2}) + " (Expected: 5)");
        System.out.println("canJump([2,3,1,1,4]) = " + canJump(new int[]{2, 3, 1, 1, 4}) + " (Expected: true)");

        // Session 7: Binary Search I
        System.out.println("\n--- [Session 7: Binary Search I] ---");
        int[] sortedArr = {1, 3, 5, 5, 5, 7, 9};
        System.out.println("binarySearch([1,3,5,5,5,7,9], 7) = " + binarySearch(sortedArr, 7) + " (Expected: 5)");
        System.out.println("lowerBound(5) = " + lowerBound(sortedArr, 5) + " (Expected: 2)");
        System.out.println("upperBound(5) = " + upperBound(sortedArr, 5) + " (Expected: 5)");
        System.out.println("searchRange(5) = " + Arrays.toString(searchRange(sortedArr, 5)) + " (Expected: [2, 4])");
        System.out.println("minEatingSpeed([3,6,7,11], 8) = " + minEatingSpeed(new int[]{3, 6, 7, 11}, 8) + " (Expected: 4)");
        System.out.println("searchInsert([1,3,5,6], 2) = " + searchInsert(new int[]{1, 3, 5, 6}, 2) + " (Expected: 1)");
        System.out.println("arrangeCoins(5) = " + arrangeCoins(5) + " (Expected: 2)");
        System.out.println("nextGreatestLetter(['c','f','j'], 'c') = " + nextGreatestLetter(new char[]{'c', 'f', 'j'}, 'c') + " (Expected: f)");
        System.out.println("findPeakElement([1,2,3,1]) = " + findPeakElement(new int[]{1, 2, 3, 1}) + " (Expected: 2)");

        // Session 8: Binary Search II
        System.out.println("\n--- [Session 8: Binary Search II] ---");
        System.out.println("searchRotated([4,5,6,7,0,1,2], 0) = " + searchRotated(new int[]{4, 5, 6, 7, 0, 1, 2}, 0) + " (Expected: 4)");
        System.out.println("findMinRotated([3,4,5,1,2]) = " + findMinRotated(new int[]{3, 4, 5, 1, 2}) + " (Expected: 1)");
        System.out.println("peakIndexInMountainArray([0,2,10,5,2]) = " + peakIndexInMountainArray(new int[]{0, 2, 10, 5, 2}) + " (Expected: 2)");
        System.out.println("findInMountainArray(3, [1,2,3,4,5,3,1]) = " + findInMountainArray(3, new int[]{1, 2, 3, 4, 5, 3, 1}) + " (Expected: 2)");
        System.out.println("maxDistance([1,2,3,4,7], 3) = " + maxDistance(new int[]{1, 2, 3, 4, 7}, 3) + " (Expected: 3)");
        System.out.println("shipWithinDays([1..10], 5) = " + shipWithinDays(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 5) + " (Expected: 15)");

        // Session 9: Matrix Problems I
        System.out.println("\n--- [Session 9: Matrix Problems I] ---");
        int[][] mat1 = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        System.out.println("spiralOrder = " + spiralOrder(mat1) + " (Expected: [1, 2, 3, 6, 9, 8, 7, 4, 5])");
        System.out.println("searchMatrix(mat1, 5) = " + searchMatrix(mat1, 5) + " (Expected: true)");
        System.out.println("sortedMatrixElements = " + sortedMatrixElements(mat1));

        // Session 10: Matrix Problems II
        System.out.println("\n--- [Session 10: Matrix Problems II] ---");
        int[][] mat2 = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        System.out.println("diagonalSum = " + diagonalSum(mat2) + " (Expected: 25)");
        System.out.println("matrixReshape([[1,2],[3,4]], 1, 4) = " + Arrays.deepToString(matrixReshape(new int[][]{{1, 2}, {3, 4}}, 1, 4)));
        System.out.println("isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]) = " + isToeplitzMatrix(new int[][]{{1, 2, 3, 4}, {5, 1, 2, 3}, {9, 5, 1, 2}}) + " (Expected: true)");
        System.out.println("findDiagonalOrder = " + Arrays.toString(findDiagonalOrder(mat2)) + " (Expected: [1, 2, 4, 7, 5, 3, 6, 8, 9])");
        System.out.println("searchMatrixII = " + searchMatrixII(mat2, 6) + " (Expected: true)");
        int[][] sortedMat = {{1, 3, 5}, {2, 6, 9}, {3, 6, 9}};
        System.out.println("matrixMedian = " + matrixMedian(sortedMat) + " (Expected: 5)");
        int[][] binMat = {{0, 0, 1, 1}, {0, 1, 1, 1}, {0, 0, 0, 1}};
        System.out.println("rowWithMaxOnes = " + rowWithMaxOnes(binMat) + " (Expected: 1)");
        int[][] rotMat = {{1, 2}, {3, 4}};
        rotateImage(rotMat);
        System.out.println("rotateImage([[1,2],[3,4]]) = " + Arrays.deepToString(rotMat) + " (Expected: [[3, 1], [4, 2]])");
        System.out.println("flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]) = " + Arrays.deepToString(flipAndInvertImage(new int[][]{{1, 1, 0}, {1, 0, 1}, {0, 0, 0}})));
        System.out.println("countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]) = " + countNegatives(new int[][]{{4, 3, 2, -1}, {3, 2, 1, -1}, {1, 1, -1, -2}, {-1, -1, -2, -3}}) + " (Expected: 8)");

        // Session 11: Strings I
        System.out.println("\n--- [Session 11: Strings I] ---");
        System.out.println("characterFrequency(\"banana\", 'a') = " + characterFrequency("banana", 'a') + " (Expected: 3)");
        System.out.println("countWords(\"   Competitive  Coding  Bank  \") = " + countWords("   Competitive  Coding  Bank  ") + " (Expected: 3)");
        System.out.println("isIsomorphic(\"egg\", \"add\") = " + isIsomorphic("egg", "add") + " (Expected: true)");
        System.out.println("toLowerCaseSimple(\"Hello World\") = " + toLowerCaseSimple("Hello World") + " (Expected: hello world)");
        System.out.println("reverseStr(\"abcdefg\", 2) = " + reverseStr("abcdefg", 2) + " (Expected: bacdfeg)");
        System.out.println("findTheDifference(\"abcd\", \"abcde\") = " + findTheDifference("abcd", "abcde") + " (Expected: e)");
        System.out.println("canConstruct(\"aa\", \"aab\") = " + canConstruct("aa", "aab") + " (Expected: true)");
        System.out.println("wordPattern(\"abba\", \"dog cat cat dog\") = " + wordPattern("abba", "dog cat cat dog") + " (Expected: true)");
        System.out.println("areAlmostEqual(\"bank\", \"kanb\") = " + areAlmostEqual("bank", "kanb") + " (Expected: true)");
        System.out.println("areAlmostEqual(\"bank\", \"kan\") = " + areAlmostEqual("bank", "kan") + " (Expected: false)");

        // Session 12: Strings II
        System.out.println("\n--- [Session 12: Strings II] ---");
        System.out.println("isAnagram(\"anagram\", \"nagaram\") = " + isAnagram("anagram", "nagaram") + " (Expected: true)");
        System.out.println("longestCommonPrefix([\"flower\",\"flow\",\"flight\"]) = " + longestCommonPrefix(new String[]{"flower", "flow", "flight"}) + " (Expected: fl)");
        System.out.println("minRepeats(\"abcd\", \"cdabcdab\") = " + minRepeats("abcd", "cdabcdab") + " (Expected: 3)");
        System.out.println("isPalindrome(\"A man, a plan, a canal: Panama\") = " + isPalindrome("A man, a plan, a canal: Panama") + " (Expected: true)");
        System.out.println("reverseWords(\"Let's take LeetCode contest\") = " + reverseWords("Let's take LeetCode contest"));
        System.out.println("repeatedSubstringPattern(\"abab\") = " + repeatedSubstringPattern("abab") + " (Expected: true)");
        System.out.println("strStr(\"sadbutsad\", \"sad\") = " + strStr("sadbutsad", "sad") + " (Expected: 0)");
        System.out.println("longestPrefix(\"level\") = " + longestPrefix("level") + " (Expected: l)");

        // Session 13-15: Linked Lists
        System.out.println("\n--- [Session 13-15: Linked Lists] ---");
        ListNode head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        System.out.print("Original list: ");
        printList(head);

        head = reverseList(head);
        System.out.print("Reversed list: ");
        printList(head); // 5 -> 4 -> 3 -> 2 -> 1

        head = reverseList(head); // restore to 1 -> 2 -> 3 -> 4 -> 5
        System.out.println("Middle node value: " + middleNode(head).val + " (Expected: 3)");

        ListNode l1 = new ListNode(1, new ListNode(2, new ListNode(4)));
        ListNode l2 = new ListNode(1, new ListNode(3, new ListNode(4)));
        System.out.print("mergeTwoLists: ");
        printList(mergeTwoLists(l1, l2)); // 1 -> 1 -> 2 -> 3 -> 4 -> 4

        ListNode delTest = new ListNode(1, new ListNode(2, new ListNode(6, new ListNode(3, new ListNode(4, new ListNode(5, new ListNode(6)))))));
        System.out.print("removeElements(val=6): ");
        printList(removeElements(delTest, 6)); // 1 -> 2 -> 3 -> 4 -> 5

        ListNode dupTest = new ListNode(1, new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(3)))));
        System.out.print("deleteDuplicates: ");
        printList(deleteDuplicates(dupTest)); // 1 -> 2 -> 3

        ListNode addL1 = new ListNode(2, new ListNode(4, new ListNode(3)));
        ListNode addL2 = new ListNode(5, new ListNode(6, new ListNode(4)));
        System.out.print("addTwoNumbers (342 + 465 = 807): ");
        printList(addTwoNumbers(addL1, addL2)); // 7 -> 0 -> 8

        ListNode rotList = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        System.out.print("rotateRightList(k=2): ");
        printList(rotateRightList(rotList, 2)); // 4 -> 5 -> 1 -> 2 -> 3

        ListNode oddEven = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        System.out.print("oddEvenList: ");
        printList(oddEvenList(oddEven)); // 1 -> 3 -> 5 -> 2 -> 4

        ListNode sortL = new ListNode(4, new ListNode(2, new ListNode(1, new ListNode(3))));
        System.out.print("sortList: ");
        printList(sortList(sortL)); // 1 -> 2 -> 3 -> 4

        ListNode doubleL = new ListNode(1, new ListNode(8, new ListNode(9)));
        System.out.print("doubleIt (189 * 2 = 378): ");
        printList(doubleIt(doubleL)); // 3 -> 7 -> 8

        System.out.println("\n==================================================");
        System.out.println("  ALL SESSIONS EXECUTED SUCCESSFULLY!");
        System.out.println("==================================================");
    }
}
