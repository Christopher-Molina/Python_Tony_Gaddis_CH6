def main():
    # Input student name
    student_name = input('Enter your name: ')

    # Input student description
    student_description = input('Describe yourself: ')

    # Create html file and write data to it
    with open('student.html', 'w') as outfile:
        outfile.write('<html>\n')
        outfile.write('<head>\n')
        outfile.write('</head>\n')
        outfile.write('<body>\n')
        outfile.write('     <center>\n')
        outfile.write('         <h1>' + student_name + '</h1>\n')
        outfile.write('     </center.\n')
        outfile.write('     <hr />\n')
        outfile.write('     ' + student_description + '\n')
        outfile.write('     <hr />\n')
        outfile.write('</body>')
        outfile.write('</html>')


# Call the main function
if __name__ == '__main__':
    main()