result = []
ARGV.each do |arg|
    next if arg !~ /^-?[0-9]+$/
    result << arg.to_i
end
puts result.sort
